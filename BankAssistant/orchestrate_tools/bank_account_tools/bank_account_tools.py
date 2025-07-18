from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import datetime, timedelta

# Sample bank account data
BANK_ACCOUNTS = [
    # Arnold Palmer's Accounts
    {
        "accountId": "BA1001",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "accountType": "Checking",
        "accountNumber": "****1234",
        "nickname": "Primary Checking",
        "status": "Active",
        "balance": 75000.00,
        "availableBalance": 70000.00,
        "interestRate": 0.01,
        "openingDate": "2020-01-15",
        "lastActivityDate": "2024-03-20",
        "monthlyFee": 0.00,
        "minimumBalance": 0.00,
        "overdraftProtection": True,
        "overdraftLimit": 5000.00,
        "directDeposit": True,
        "billPayEnabled": True,
        "zelleEnabled": True,
        "recentTransactions": [
            {
                "transactionId": "T1001",
                "date": "2024-03-20",
                "description": "Credit Card Payment",
                "amount": -1250.00,
                "type": "ACH",
                "status": "Completed",
                "category": "Credit Card Payment"
            },
            {
                "transactionId": "T1002",
                "date": "2024-03-19",
                "description": "Investment Transfer",
                "amount": -10000.00,
                "type": "Transfer",
                "status": "Completed",
                "category": "Investment"
            }
        ]
    },
    {
        "accountId": "BA1002",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "accountType": "Savings",
        "accountNumber": "****5678",
        "nickname": "Emergency Fund",
        "status": "Active",
        "balance": 150000.00,
        "availableBalance": 150000.00,
        "interestRate": 4.25,
        "openingDate": "2020-01-15",
        "lastActivityDate": "2024-03-15",
        "monthlyFee": 0.00,
        "minimumBalance": 10000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": False,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T1003",
                "date": "2024-03-15",
                "description": "Interest Payment",
                "amount": 531.25,
                "type": "Interest",
                "status": "Completed",
                "category": "Interest"
            }
        ]
    },
    {
        "accountId": "BA1003",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "accountType": "Money Market",
        "accountNumber": "****9012",
        "nickname": "Investment Buffer",
        "status": "Active",
        "balance": 500000.00,
        "availableBalance": 500000.00,
        "interestRate": 4.50,
        "openingDate": "2021-06-01",
        "lastActivityDate": "2024-03-20",
        "monthlyFee": 0.00,
        "minimumBalance": 25000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": True,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T1004",
                "date": "2024-03-20",
                "description": "Investment Transfer",
                "amount": -50000.00,
                "type": "Transfer",
                "status": "Completed",
                "category": "Investment"
            }
        ]
    },
    # Jack Nicklaus's Accounts
    {
        "accountId": "BA2001",
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "accountType": "Checking",
        "accountNumber": "****3456",
        "nickname": "Primary Checking",
        "status": "Active",
        "balance": 200000.00,
        "availableBalance": 190000.00,
        "interestRate": 0.01,
        "openingDate": "2019-03-15",
        "lastActivityDate": "2024-03-15",
        "monthlyFee": 0.00,
        "minimumBalance": 0.00,
        "overdraftProtection": True,
        "overdraftLimit": 10000.00,
        "directDeposit": True,
        "billPayEnabled": True,
        "zelleEnabled": True,
        "recentTransactions": [
            {
                "transactionId": "T2001",
                "date": "2024-03-15",
                "description": "Credit Card Payment",
                "amount": -2500.00,
                "type": "ACH",
                "status": "Completed",
                "category": "Credit Card Payment"
            }
        ]
    },
    {
        "accountId": "BA2002",
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "accountType": "Savings",
        "accountNumber": "****7890",
        "nickname": "Savings Account",
        "status": "Active",
        "balance": 300000.00,
        "availableBalance": 300000.00,
        "interestRate": 4.50,
        "openingDate": "2019-03-15",
        "lastActivityDate": "2024-03-15",
        "monthlyFee": 0.00,
        "minimumBalance": 10000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": False,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T2002",
                "date": "2024-03-15",
                "description": "Interest Payment",
                "amount": 1125.00,
                "type": "Interest",
                "status": "Completed",
                "category": "Interest"
            }
        ]
    },
    # Annika Sorenstam's Accounts
    {
        "accountId": "BA3001",
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "accountType": "Checking",
        "accountNumber": "****2345",
        "nickname": "Primary Checking",
        "status": "Active",
        "balance": 100000.00,
        "availableBalance": 95000.00,
        "interestRate": 0.01,
        "openingDate": "2021-06-01",
        "lastActivityDate": "2024-03-20",
        "monthlyFee": 0.00,
        "minimumBalance": 0.00,
        "overdraftProtection": True,
        "overdraftLimit": 5000.00,
        "directDeposit": True,
        "billPayEnabled": True,
        "zelleEnabled": True,
        "recentTransactions": [
            {
                "transactionId": "T3001",
                "date": "2024-03-20",
                "description": "Credit Card Payment",
                "amount": -1500.00,
                "type": "ACH",
                "status": "Completed",
                "category": "Credit Card Payment"
            }
        ]
    },
    {
        "accountId": "BA3002",
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "accountType": "Savings",
        "accountNumber": "****6789",
        "nickname": "Savings Account",
        "status": "Active",
        "balance": 200000.00,
        "availableBalance": 200000.00,
        "interestRate": 4.25,
        "openingDate": "2021-06-01",
        "lastActivityDate": "2024-03-20",
        "monthlyFee": 0.00,
        "minimumBalance": 10000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": False,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T3002",
                "date": "2024-03-20",
                "description": "Interest Payment",
                "amount": 708.33,
                "type": "Interest",
                "status": "Completed",
                "category": "Interest"
            }
        ]
    },
    # Gary Player's Accounts
    {
        "accountId": "BA4001",
        "userId": "U4001",
        "userName": "Gary Player",
        "accountType": "Checking",
        "accountNumber": "****3456",
        "nickname": "Primary Checking",
        "status": "Active",
        "balance": 300000.00,
        "availableBalance": 290000.00,
        "interestRate": 0.01,
        "openingDate": "2018-09-15",
        "lastActivityDate": "2024-03-05",
        "monthlyFee": 0.00,
        "minimumBalance": 0.00,
        "overdraftProtection": True,
        "overdraftLimit": 15000.00,
        "directDeposit": True,
        "billPayEnabled": True,
        "zelleEnabled": True,
        "recentTransactions": [
            {
                "transactionId": "T4001",
                "date": "2024-03-05",
                "description": "Credit Card Payment",
                "amount": -3750.00,
                "type": "ACH",
                "status": "Completed",
                "category": "Credit Card Payment"
            }
        ]
    },
    {
        "accountId": "BA4002",
        "userId": "U4001",
        "userName": "Gary Player",
        "accountType": "Savings",
        "accountNumber": "****7890",
        "nickname": "Savings Account",
        "status": "Active",
        "balance": 400000.00,
        "availableBalance": 400000.00,
        "interestRate": 4.50,
        "openingDate": "2018-09-15",
        "lastActivityDate": "2024-03-05",
        "monthlyFee": 0.00,
        "minimumBalance": 10000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": False,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T4002",
                "date": "2024-03-05",
                "description": "Interest Payment",
                "amount": 1500.00,
                "type": "Interest",
                "status": "Completed",
                "category": "Interest"
            }
        ]
    },
    # Phil Mickelson's Accounts
    {
        "accountId": "BA5001",
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "accountType": "Checking",
        "accountNumber": "****4567",
        "nickname": "Primary Checking",
        "status": "Active",
        "balance": 400000.00,
        "availableBalance": 390000.00,
        "interestRate": 0.01,
        "openingDate": "2017-12-01",
        "lastActivityDate": "2024-03-15",
        "monthlyFee": 0.00,
        "minimumBalance": 0.00,
        "overdraftProtection": True,
        "overdraftLimit": 20000.00,
        "directDeposit": True,
        "billPayEnabled": True,
        "zelleEnabled": True,
        "recentTransactions": [
            {
                "transactionId": "T5001",
                "date": "2024-03-15",
                "description": "Credit Card Payment",
                "amount": -5000.00,
                "type": "ACH",
                "status": "Completed",
                "category": "Credit Card Payment"
            }
        ]
    },
    {
        "accountId": "BA5002",
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "accountType": "Savings",
        "accountNumber": "****8901",
        "nickname": "Savings Account",
        "status": "Active",
        "balance": 500000.00,
        "availableBalance": 500000.00,
        "interestRate": 4.50,
        "openingDate": "2017-12-01",
        "lastActivityDate": "2024-03-15",
        "monthlyFee": 0.00,
        "minimumBalance": 10000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": False,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T5002",
                "date": "2024-03-15",
                "description": "Interest Payment",
                "amount": 1875.00,
                "type": "Interest",
                "status": "Completed",
                "category": "Interest"
            }
        ]
    },
    # Seve Ballesteros's Accounts
    {
        "accountId": "BA6001",
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "accountType": "Checking",
        "accountNumber": "****5678",
        "nickname": "Primary Checking",
        "status": "Active",
        "balance": 150000.00,
        "availableBalance": 145000.00,
        "interestRate": 0.01,
        "openingDate": "2020-06-15",
        "lastActivityDate": "2024-03-10",
        "monthlyFee": 0.00,
        "minimumBalance": 0.00,
        "overdraftProtection": True,
        "overdraftLimit": 7500.00,
        "directDeposit": True,
        "billPayEnabled": True,
        "zelleEnabled": True,
        "recentTransactions": [
            {
                "transactionId": "T6001",
                "date": "2024-03-10",
                "description": "Credit Card Payment",
                "amount": -3000.00,
                "type": "ACH",
                "status": "Completed",
                "category": "Credit Card Payment"
            }
        ]
    },
    {
        "accountId": "BA6002",
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "accountType": "Savings",
        "accountNumber": "****9012",
        "nickname": "Savings Account",
        "status": "Active",
        "balance": 250000.00,
        "availableBalance": 250000.00,
        "interestRate": 4.25,
        "openingDate": "2020-06-15",
        "lastActivityDate": "2024-03-10",
        "monthlyFee": 0.00,
        "minimumBalance": 10000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": False,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T6002",
                "date": "2024-03-10",
                "description": "Interest Payment",
                "amount": 885.42,
                "type": "Interest",
                "status": "Completed",
                "category": "Interest"
            }
        ]
    },
    # Greg Norman's Accounts
    {
        "accountId": "BA7001",
        "userId": "U7001",
        "userName": "Greg Norman",
        "accountType": "Checking",
        "accountNumber": "****6789",
        "nickname": "Primary Checking",
        "status": "Active",
        "balance": 350000.00,
        "availableBalance": 340000.00,
        "interestRate": 0.01,
        "openingDate": "2019-03-01",
        "lastActivityDate": "2024-03-20",
        "monthlyFee": 0.00,
        "minimumBalance": 0.00,
        "overdraftProtection": True,
        "overdraftLimit": 17500.00,
        "directDeposit": True,
        "billPayEnabled": True,
        "zelleEnabled": True,
        "recentTransactions": [
            {
                "transactionId": "T7001",
                "date": "2024-03-20",
                "description": "Credit Card Payment",
                "amount": -4250.00,
                "type": "ACH",
                "status": "Completed",
                "category": "Credit Card Payment"
            }
        ]
    },
    {
        "accountId": "BA7002",
        "userId": "U7001",
        "userName": "Greg Norman",
        "accountType": "Savings",
        "accountNumber": "****0123",
        "nickname": "Savings Account",
        "status": "Active",
        "balance": 450000.00,
        "availableBalance": 450000.00,
        "interestRate": 4.50,
        "openingDate": "2019-03-01",
        "lastActivityDate": "2024-03-20",
        "monthlyFee": 0.00,
        "minimumBalance": 10000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": False,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T7002",
                "date": "2024-03-20",
                "description": "Interest Payment",
                "amount": 1687.50,
                "type": "Interest",
                "status": "Completed",
                "category": "Interest"
            }
        ]
    },
    # Tiger Woods's Accounts
    {
        "accountId": "BA8001",
        "userId": "U8001",
        "userName": "Tiger Woods",
        "accountType": "Checking",
        "accountNumber": "****7890",
        "nickname": "Primary Checking",
        "status": "Active",
        "balance": 250000.00,
        "availableBalance": 240000.00,
        "interestRate": 0.01,
        "openingDate": "2019-03-15",
        "lastActivityDate": "2024-03-15",
        "monthlyFee": 0.00,
        "minimumBalance": 0.00,
        "overdraftProtection": True,
        "overdraftLimit": 12500.00,
        "directDeposit": True,
        "billPayEnabled": True,
        "zelleEnabled": True,
        "recentTransactions": [
            {
                "transactionId": "T8001",
                "date": "2024-03-15",
                "description": "Credit Card Payment",
                "amount": -4000.00,
                "type": "ACH",
                "status": "Completed",
                "category": "Credit Card Payment"
            }
        ]
    },
    {
        "accountId": "BA8002",
        "userId": "U8001",
        "userName": "Tiger Woods",
        "accountType": "Savings",
        "accountNumber": "****1234",
        "nickname": "Savings Account",
        "status": "Active",
        "balance": 350000.00,
        "availableBalance": 350000.00,
        "interestRate": 4.25,
        "openingDate": "2019-03-15",
        "lastActivityDate": "2024-03-15",
        "monthlyFee": 0.00,
        "minimumBalance": 10000.00,
        "overdraftProtection": False,
        "overdraftLimit": 0.00,
        "directDeposit": False,
        "billPayEnabled": False,
        "zelleEnabled": False,
        "recentTransactions": [
            {
                "transactionId": "T8002",
                "date": "2024-03-15",
                "description": "Interest Payment",
                "amount": 1239.58,
                "type": "Interest",
                "status": "Completed",
                "category": "Interest"
            }
        ]
    }
]

# Sample account alerts and notifications
ACCOUNT_ALERTS = [
    {
        "alertId": "A1001",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "accountId": "BA1001",
        "type": "Low Balance",
        "description": "Checking account balance below $100,000",
        "severity": "Medium",
        "date": "2024-03-20",
        "status": "Active"
    },
    {
        "alertId": "A1002",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "accountId": "BA1002",
        "type": "Interest Rate Change",
        "description": "Savings account interest rate increased to 4.25%",
        "severity": "Low",
        "date": "2024-03-15",
        "status": "Active"
    },
    {
        "alertId": "A2001",
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "accountId": "BA2001",
        "type": "Low Balance",
        "description": "Checking account balance below $250,000",
        "severity": "Medium",
        "date": "2024-03-15",
        "status": "Active"
    },
    {
        "alertId": "A3001",
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "accountId": "BA3001",
        "type": "Low Balance",
        "description": "Checking account balance below $150,000",
        "severity": "Medium",
        "date": "2024-03-20",
        "status": "Active"
    },
    {
        "alertId": "A4001",
        "userId": "U4001",
        "userName": "Gary Player",
        "accountId": "BA4001",
        "type": "Low Balance",
        "description": "Checking account balance below $350,000",
        "severity": "Medium",
        "date": "2024-03-05",
        "status": "Active"
    },
    {
        "alertId": "A5001",
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "accountId": "BA5001",
        "type": "Low Balance",
        "description": "Checking account balance below $450,000",
        "severity": "Medium",
        "date": "2024-03-15",
        "status": "Active"
    },
    {
        "alertId": "A6001",
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "accountId": "BA6001",
        "type": "Low Balance",
        "description": "Checking account balance below $200,000",
        "severity": "Medium",
        "date": "2024-03-10",
        "status": "Active"
    },
    {
        "alertId": "A7001",
        "userId": "U7001",
        "userName": "Greg Norman",
        "accountId": "BA7001",
        "type": "Low Balance",
        "description": "Checking account balance below $400,000",
        "severity": "Medium",
        "date": "2024-03-20",
        "status": "Active"
    },
    {
        "alertId": "A8001",
        "userId": "U8001",
        "userName": "Tiger Woods",
        "accountId": "BA8001",
        "type": "Low Balance",
        "description": "Checking account balance below $300,000",
        "severity": "Medium",
        "date": "2024-03-15",
        "status": "Active"
    }
]

@tool
def get_bank_accounts(userId: str = None, userName: str = None):
    """
    Retrieve detailed information about bank accounts for a specific user (if provided), including balances, transactions, and account features.

    :param userId: (optional) Unique identifier for the account holder (matches 'userId' in the data)
    :param userName: (optional) Name of the account holder (matches 'userName' in the data)
    :returns: A list of dictionaries, each containing details about a specific bank account:
              - 'accountId': Unique identifier for the account
              - 'userId': Unique identifier for the account holder
              - 'userName': Name of the account holder
              - 'accountType': Type of account (Checking, Savings, Money Market)
              - 'accountNumber': Masked account number
              - 'nickname': Account nickname
              - 'status': Current status of the account
              - 'balance': Current balance
              - 'availableBalance': Available balance
              - 'interestRate': Current interest rate
              - 'openingDate': Account opening date
              - 'lastActivityDate': Date of last activity
              - 'monthlyFee': Monthly maintenance fee
              - 'minimumBalance': Minimum balance requirement
              - 'overdraftProtection': Whether overdraft protection is enabled
              - 'overdraftLimit': Overdraft protection limit
              - 'directDeposit': Whether direct deposit is enabled
              - 'billPayEnabled': Whether bill pay is enabled
              - 'zelleEnabled': Whether Zelle is enabled
              - 'recentTransactions': List of recent transactions
    """
    results = BANK_ACCOUNTS
    if userId:
        results = [acc for acc in results if acc["userId"] == userId]
    if userName:
        results = [acc for acc in results if acc["userName"].lower() == userName.lower()]
    return results

@tool
def get_account_alerts(userId: str = None, userName: str = None):
    """
    Retrieve account alerts and notifications for a specific user (if provided).

    :param userId: (optional) Unique identifier for the account holder (matches 'userId' in the data)
    :param userName: (optional) Name of the account holder (matches 'userName' in the data)
    :returns: A list of dictionaries, each containing details about a specific alert:
              - 'alertId': Unique identifier for the alert
              - 'userId': Unique identifier for the account holder
              - 'userName': Name of the account holder
              - 'accountId': ID of the account
              - 'type': Type of alert
              - 'description': Alert description
              - 'severity': Alert severity level
              - 'date': Alert date
              - 'status': Alert status
    """
    results = ACCOUNT_ALERTS
    if userId:
        results = [a for a in results if a["userId"] == userId]
    if userName:
        results = [a for a in results if a["userName"].lower() == userName.lower()]
    return results

@tool
def get_total_balance(userId: str = None, userName: str = None):
    """
    Calculate total balance across all accounts for a specific user.
    Accepts either userId or userName.

    :param userId: (optional) Unique identifier for the user
    :param userName: (optional) Name of the user (case-insensitive)
    :returns: A dictionary containing:
        - 'userId': User identifier
        - 'userName': Name of the user
        - 'totalBalance': Total balance across all accounts
        - 'accountBreakdown': Dictionary of balances by account type
        - 'availableBalance': Total available balance
        Or an error if not found.
    """
    if not userId and userName:
        user_id_result = get_user_id_by_name(userName)
        if 'userId' not in user_id_result:
            return {"error": f"User with name '{userName}' not found"}
        userId = user_id_result['userId']
    if not userId:
        return {"error": "No userId or userName provided"}
    user_accounts = [acc for acc in BANK_ACCOUNTS if acc["userId"] == userId]
    if not user_accounts:
        return {"error": "User not found"}
    total_balance = sum(acc["balance"] for acc in user_accounts)
    available_balance = sum(acc["availableBalance"] for acc in user_accounts)
    account_breakdown = {
        "checking": sum(acc["balance"] for acc in user_accounts if acc["accountType"] == "Checking"),
        "savings": sum(acc["balance"] for acc in user_accounts if acc["accountType"] == "Savings"),
        "moneyMarket": sum(acc["balance"] for acc in user_accounts if acc["accountType"] == "Money Market")
    }
    return {
        "userId": userId,
        "userName": user_accounts[0]["userName"],
        "totalBalance": total_balance,
        "accountBreakdown": account_breakdown,
        "availableBalance": available_balance
    }

@tool
def get_account_transactions(account_id: str, start_date: str = None, end_date: str = None):
    """
    Retrieve transactions for a specific account within a date range.

    :param account_id: Unique identifier for the account
    :param start_date: Optional start date for transaction range (YYYY-MM-DD)
    :param end_date: Optional end date for transaction range (YYYY-MM-DD)
    :returns: A dictionary containing transaction information:
              - 'accountId': Account identifier
              - 'accountType': Type of account
              - 'transactions': List of transactions
              - 'summary': Transaction summary statistics
    """
    account = next((acc for acc in BANK_ACCOUNTS if acc["accountId"] == account_id), None)
    if not account:
        return {"error": "Account not found"}
    
    transactions = account["recentTransactions"]
    
    if start_date and end_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        transactions = [
            t for t in transactions 
            if start <= datetime.strptime(t["date"], "%Y-%m-%d") <= end
        ]
    
    summary = {
        "totalTransactions": len(transactions),
        "totalDebits": sum(t["amount"] for t in transactions if t["amount"] < 0),
        "totalCredits": sum(t["amount"] for t in transactions if t["amount"] > 0),
        "averageTransaction": sum(t["amount"] for t in transactions) / len(transactions) if transactions else 0
    }
    
    return {
        "accountId": account_id,
        "accountType": account["accountType"],
        "transactions": transactions,
        "summary": summary
    }

@tool
def get_financial_summary(userId: str):
    """
    Get a comprehensive financial summary including bank accounts, credit cards,
    and investments for a specific user.

    :param userId: Unique identifier for the user
    :returns: A dictionary containing comprehensive financial information:
              - 'userId': User identifier
              - 'userName': Name of the user
              - 'bankAccounts': Summary of bank accounts
              - 'creditCards': Summary of credit cards
              - 'investments': Summary of investments
              - 'totalAssets': Total assets
              - 'totalLiabilities': Total liabilities
              - 'netWorth': Net worth
    """
    # This would typically integrate with credit card and investment tools
    # Here we're returning sample data
    user_accounts = [acc for acc in BANK_ACCOUNTS if acc["userId"] == userId]
    if not user_accounts:
        return {"error": "User not found"}
    
    total_assets = sum(acc["balance"] for acc in user_accounts)
    
    # Sample credit card and investment data (would come from other tools)
    credit_cards = {
        "totalBalance": 9250.00,  # Sum of Arnold's credit card balances
        "availableCredit": 30750.00,
        "totalLimit": 40000.00
    }
    
    investments = {
        "totalValue": 2500000.00,  # Arnold's investment portfolio value
        "ytdReturn": 7.8,
        "oneYearReturn": 11.5
    }
    
    return {
        "userId": userId,
        "userName": user_accounts[0]["userName"],
        "bankAccounts": {
            "totalBalance": total_assets,
            "accountCount": len(user_accounts),
            "accountTypes": list(set(acc["accountType"] for acc in user_accounts))
        },
        "creditCards": credit_cards,
        "investments": investments,
        "totalAssets": total_assets + investments["totalValue"],
        "totalLiabilities": credit_cards["totalBalance"],
        "netWorth": total_assets + investments["totalValue"] - credit_cards["totalBalance"]
    }

@tool
def get_user_id_by_name(userName: str):
    """
    Look up a user's ID by their name.

    :param userName: Name of the user (case-insensitive)
    :returns: A dictionary with 'userId' if found, or an error message if not found.
    """
    for acc in BANK_ACCOUNTS:
        if acc["userName"].lower() == userName.lower():
            return {"userId": acc["userId"]}
    return {"error": f"User with name '{userName}' not found"} 