from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
import requests
from bs4 import BeautifulSoup

@tool(name='read_web_pages', description='Reads a web page and returns its content', permission=ToolPermission.READ_ONLY)
def get_mortgage_rates():
    """
    Fetch current US mortgage rates from Freddie Mac's PMMS archive page.

    :returns: A dictionary containing current mortgage rates, e.g.:
        - '30_year_fixed': 6.75
        - '15_year_fixed': 6.10
        Or an error message if unavailable.
    """
    url = "https://www.freddiemac.com/pmms/archive"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Find the first table with rates (should be the most recent week)
        table = soup.find("table")
        if not table:
            return {"error": "Could not find rates table on Freddie Mac page."}
        rows = table.find_all("tr")
        if len(rows) < 2:
            return {"error": "Rates table missing data rows."}
        # The first row is header, the second row is the latest data
        header = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]
        data = [td.get_text(strip=True) for td in rows[1].find_all("td")]
        # Expecting: ["Average Rates", "6.67%", "5.80%", ...]
        if len(data) < 3:
            return {"error": "Unexpected rates table format."}
        try:
            rate_30 = float(data[1].replace("%", ""))
            rate_15 = float(data[2].replace("%", ""))
        except Exception:
            return {"error": "Could not parse rate values."}
        return {
            "30_year_fixed": rate_30,
            "15_year_fixed": rate_15
        }
    except Exception as e:
        return {"error": f"Failed to fetch rates: {str(e)}"}

@tool
def calculate_mortgage_payment(principal: float, annual_rate: float, years: int, down_payment: float = 0):
    """
    Calculate the monthly mortgage payment and summary based on user inputs.

    :param principal: Total loan amount (float)
    :param annual_rate: Annual interest rate as a percentage (e.g., 6.5 for 6.5%)
    :param years: Loan term in years (int)
    :param down_payment: Down payment amount (float, default 0)
    :returns: A dictionary containing:
        - 'monthly_payment': Calculated monthly payment (float)
        - 'total_payment': Total payment over the loan (float)
        - 'total_interest': Total interest paid (float)
        - 'inputs': Echo of input parameters
        Or an error message if inputs are invalid.
    """
    try:
        if principal <= 0 or annual_rate <= 0 or years <= 0:
            return {"error": "Principal, annual_rate, and years must be positive numbers."}
        loan_amount = principal - down_payment
        if loan_amount <= 0:
            return {"error": "Down payment must be less than principal."}
        n = years * 12
        r = (annual_rate / 100) / 12
        # Amortization formula
        monthly_payment = loan_amount * r * (1 + r) ** n / ((1 + r) ** n - 1)
        total_payment = monthly_payment * n
        total_interest = total_payment - loan_amount
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2),
            "inputs": {
                "principal": principal,
                "annual_rate": annual_rate,
                "years": years,
                "down_payment": down_payment
            }
        }
    except Exception as e:
        return {"error": f"Failed to calculate mortgage payment: {str(e)}"}
