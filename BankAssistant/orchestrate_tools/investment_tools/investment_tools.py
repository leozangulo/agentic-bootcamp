from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import datetime, timedelta

# Sample investment portfolio data
INVESTMENT_PORTFOLIOS = [
    # Arnold Palmer's Portfolio
    {
        "portfolioId": "P1001",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "portfolioName": "Retirement Portfolio",
        "totalValue": 2500000.00,
        "riskProfile": "Moderate",
        "investmentGoal": "Retirement",
        "targetDate": "2035-01-01",
        "lastUpdated": "2024-03-20",
        "holdings": [
            {
                "holdingId": "H1001",
                "symbol": "VTI",
                "name": "Vanguard Total Stock Market ETF",
                "type": "ETF",
                "quantity": 1000,
                "purchasePrice": 150.00,
                "currentPrice": 165.00,
                "marketValue": 165000.00,
                "allocation": 6.6,
                "purchaseDate": "2023-01-15",
                "performance": {
                    "ytd": 8.5,
                    "oneYear": 12.3,
                    "threeYear": 35.2,
                    "fiveYear": 65.8
                }
            },
            {
                "holdingId": "H1002",
                "symbol": "VXUS",
                "name": "Vanguard Total International Stock ETF",
                "type": "ETF",
                "quantity": 500,
                "purchasePrice": 60.00,
                "currentPrice": 65.00,
                "marketValue": 32500.00,
                "allocation": 1.3,
                "purchaseDate": "2023-02-01",
                "performance": {
                    "ytd": 5.2,
                    "oneYear": 8.7,
                    "threeYear": 25.4,
                    "fiveYear": 45.6
                }
            }
        ],
        "performance": {
            "ytd": 7.8,
            "oneYear": 11.5,
            "threeYear": 32.4,
            "fiveYear": 58.9
        }
    },
    # Jack Nicklaus's Portfolio
    {
        "portfolioId": "P2001",
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "portfolioName": "Growth Portfolio",
        "totalValue": 3500000.00,
        "riskProfile": "Aggressive",
        "investmentGoal": "Wealth Growth",
        "targetDate": "2030-01-01",
        "lastUpdated": "2024-03-20",
        "holdings": [
            {
                "holdingId": "H2001",
                "symbol": "QQQ",
                "name": "Invesco QQQ Trust",
                "type": "ETF",
                "quantity": 2000,
                "purchasePrice": 200.00,
                "currentPrice": 225.00,
                "marketValue": 450000.00,
                "allocation": 12.9,
                "purchaseDate": "2023-03-15",
                "performance": {
                    "ytd": 12.5,
                    "oneYear": 18.3,
                    "threeYear": 45.2,
                    "fiveYear": 85.8
                }
            },
            {
                "holdingId": "H2002",
                "symbol": "ARKK",
                "name": "ARK Innovation ETF",
                "type": "ETF",
                "quantity": 1000,
                "purchasePrice": 80.00,
                "currentPrice": 75.00,
                "marketValue": 75000.00,
                "allocation": 2.1,
                "purchaseDate": "2023-04-01",
                "performance": {
                    "ytd": -6.2,
                    "oneYear": -8.7,
                    "threeYear": -25.4,
                    "fiveYear": 15.6
                }
            }
        ],
        "performance": {
            "ytd": 10.2,
            "oneYear": 15.5,
            "threeYear": 38.4,
            "fiveYear": 72.9
        }
    },
    # Annika Sorenstam's Portfolio
    {
        "portfolioId": "P3001",
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "portfolioName": "Balanced Portfolio",
        "totalValue": 1800000.00,
        "riskProfile": "Moderate",
        "investmentGoal": "Long-term Growth",
        "targetDate": "2040-01-01",
        "lastUpdated": "2024-03-20",
        "holdings": [
            {
                "holdingId": "H3001",
                "symbol": "VOO",
                "name": "Vanguard S&P 500 ETF",
                "type": "ETF",
                "quantity": 800,
                "purchasePrice": 300.00,
                "currentPrice": 325.00,
                "marketValue": 260000.00,
                "allocation": 14.4,
                "purchaseDate": "2023-05-15",
                "performance": {
                    "ytd": 9.5,
                    "oneYear": 15.3,
                    "threeYear": 38.2,
                    "fiveYear": 68.8
                }
            },
            {
                "holdingId": "H3002",
                "symbol": "BND",
                "name": "Vanguard Total Bond Market ETF",
                "type": "ETF",
                "quantity": 1000,
                "purchasePrice": 70.00,
                "currentPrice": 72.00,
                "marketValue": 72000.00,
                "allocation": 4.0,
                "purchaseDate": "2023-06-01",
                "performance": {
                    "ytd": 3.2,
                    "oneYear": 4.7,
                    "threeYear": 12.4,
                    "fiveYear": 18.6
                }
            }
        ],
        "performance": {
            "ytd": 8.2,
            "oneYear": 12.5,
            "threeYear": 28.4,
            "fiveYear": 52.9
        }
    },
    # Gary Player's Portfolio
    {
        "portfolioId": "P4001",
        "userId": "U4001",
        "userName": "Gary Player",
        "portfolioName": "Business Portfolio",
        "totalValue": 5000000.00,
        "riskProfile": "Conservative",
        "investmentGoal": "Business Growth",
        "targetDate": "2028-01-01",
        "lastUpdated": "2024-03-20",
        "holdings": [
            {
                "holdingId": "H4001",
                "symbol": "VYM",
                "name": "Vanguard High Dividend Yield ETF",
                "type": "ETF",
                "quantity": 3000,
                "purchasePrice": 100.00,
                "currentPrice": 110.00,
                "marketValue": 330000.00,
                "allocation": 6.6,
                "purchaseDate": "2023-07-15",
                "performance": {
                    "ytd": 7.5,
                    "oneYear": 10.3,
                    "threeYear": 28.2,
                    "fiveYear": 45.8
                }
            },
            {
                "holdingId": "H4002",
                "symbol": "VIGI",
                "name": "Vanguard International Dividend Appreciation ETF",
                "type": "ETF",
                "quantity": 2000,
                "purchasePrice": 80.00,
                "currentPrice": 85.00,
                "marketValue": 170000.00,
                "allocation": 3.4,
                "purchaseDate": "2023-08-01",
                "performance": {
                    "ytd": 6.2,
                    "oneYear": 9.7,
                    "threeYear": 22.4,
                    "fiveYear": 38.6
                }
            }
        ],
        "performance": {
            "ytd": 6.8,
            "oneYear": 9.5,
            "threeYear": 24.4,
            "fiveYear": 42.9
        }
    },
    # Phil Mickelson's Portfolio
    {
        "portfolioId": "P5001",
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "portfolioName": "High Net Worth Portfolio",
        "totalValue": 7500000.00,
        "riskProfile": "Aggressive",
        "investmentGoal": "Wealth Preservation",
        "targetDate": "2032-01-01",
        "lastUpdated": "2024-03-20",
        "holdings": [
            {
                "holdingId": "H5001",
                "symbol": "SPY",
                "name": "SPDR S&P 500 ETF",
                "type": "ETF",
                "quantity": 5000,
                "purchasePrice": 350.00,
                "currentPrice": 380.00,
                "marketValue": 1900000.00,
                "allocation": 25.3,
                "purchaseDate": "2023-09-15",
                "performance": {
                    "ytd": 10.5,
                    "oneYear": 16.3,
                    "threeYear": 42.2,
                    "fiveYear": 75.8
                }
            },
            {
                "holdingId": "H5002",
                "symbol": "TLT",
                "name": "iShares 20+ Year Treasury Bond ETF",
                "type": "ETF",
                "quantity": 2000,
                "purchasePrice": 90.00,
                "currentPrice": 85.00,
                "marketValue": 170000.00,
                "allocation": 2.3,
                "purchaseDate": "2023-10-01",
                "performance": {
                    "ytd": -2.2,
                    "oneYear": -4.7,
                    "threeYear": -15.4,
                    "fiveYear": -5.6
                }
            }
        ],
        "performance": {
            "ytd": 9.2,
            "oneYear": 14.5,
            "threeYear": 35.4,
            "fiveYear": 65.9
        }
    },
    # Seve Ballesteros's Portfolio
    {
        "portfolioId": "P6001",
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "portfolioName": "Legacy Portfolio",
        "totalValue": 4200000.00,
        "riskProfile": "Moderate",
        "investmentGoal": "Family Legacy",
        "targetDate": "2035-01-01",
        "lastUpdated": "2024-03-20",
        "holdings": [
            {
                "holdingId": "H6001",
                "symbol": "VEA",
                "name": "Vanguard FTSE Developed Markets ETF",
                "type": "ETF",
                "quantity": 3000,
                "purchasePrice": 45.00,
                "currentPrice": 48.00,
                "marketValue": 144000.00,
                "allocation": 3.4,
                "purchaseDate": "2023-11-15",
                "performance": {
                    "ytd": 6.5,
                    "oneYear": 9.3,
                    "threeYear": 22.2,
                    "fiveYear": 35.8
                }
            },
            {
                "holdingId": "H6002",
                "symbol": "VGT",
                "name": "Vanguard Information Technology ETF",
                "type": "ETF",
                "quantity": 1000,
                "purchasePrice": 400.00,
                "currentPrice": 450.00,
                "marketValue": 450000.00,
                "allocation": 10.7,
                "purchaseDate": "2023-12-01",
                "performance": {
                    "ytd": 15.2,
                    "oneYear": 25.7,
                    "threeYear": 65.4,
                    "fiveYear": 125.6
                }
            }
        ],
        "performance": {
            "ytd": 11.2,
            "oneYear": 18.5,
            "threeYear": 45.4,
            "fiveYear": 85.9
        }
    },
    # Greg Norman's Portfolio
    {
        "portfolioId": "P7001",
        "userId": "U7001",
        "userName": "Greg Norman",
        "portfolioName": "Business Empire Portfolio",
        "totalValue": 8500000.00,
        "riskProfile": "Aggressive",
        "investmentGoal": "Business Expansion",
        "targetDate": "2026-01-01",
        "lastUpdated": "2024-03-20",
        "holdings": [
            {
                "holdingId": "H7001",
                "symbol": "XLK",
                "name": "Technology Select Sector SPDR Fund",
                "type": "ETF",
                "quantity": 4000,
                "purchasePrice": 150.00,
                "currentPrice": 175.00,
                "marketValue": 700000.00,
                "allocation": 8.2,
                "purchaseDate": "2024-01-15",
                "performance": {
                    "ytd": 16.5,
                    "oneYear": 28.3,
                    "threeYear": 75.2,
                    "fiveYear": 145.8
                }
            },
            {
                "holdingId": "H7002",
                "symbol": "XLE",
                "name": "Energy Select Sector SPDR Fund",
                "type": "ETF",
                "quantity": 2000,
                "purchasePrice": 80.00,
                "currentPrice": 85.00,
                "marketValue": 170000.00,
                "allocation": 2.0,
                "purchaseDate": "2024-02-01",
                "performance": {
                    "ytd": 8.2,
                    "oneYear": 12.7,
                    "threeYear": 35.4,
                    "fiveYear": 45.6
                }
            }
        ],
        "performance": {
            "ytd": 14.2,
            "oneYear": 22.5,
            "threeYear": 58.4,
            "fiveYear": 105.9
        }
    },
    # Tiger Woods's Portfolio
    {
        "portfolioId": "P8001",
        "userId": "U8001",
        "userName": "Tiger Woods",
        "portfolioName": "Aggressive Growth Portfolio",
        "totalValue": 6000000.00,
        "riskProfile": "Aggressive",
        "investmentGoal": "Maximize Returns",
        "targetDate": "2030-01-01",
        "lastUpdated": "2024-03-20",
        "holdings": [
            {
                "holdingId": "H8001",
                "symbol": "TSLA",
                "name": "Tesla, Inc.",
                "type": "Stock",
                "quantity": 5000,
                "purchasePrice": 200.00,
                "currentPrice": 180.00,
                "marketValue": 900000.00,
                "allocation": 15.0,
                "purchaseDate": "2023-01-15",
                "performance": {
                    "ytd": -10.0,
                    "oneYear": -5.0,
                    "threeYear": 40.0,
                    "fiveYear": 500.0
                }
            },
            {
                "holdingId": "H8002",
                "symbol": "NVDA",
                "name": "NVIDIA Corporation",
                "type": "Stock",
                "quantity": 2000,
                "purchasePrice": 400.00,
                "currentPrice": 850.00,
                "marketValue": 1700000.00,
                "allocation": 28.3,
                "purchaseDate": "2023-02-01",
                "performance": {
                    "ytd": 45.0,
                    "oneYear": 200.0,
                    "threeYear": 800.0,
                    "fiveYear": 1500.0
                }
            }
        ],
        "performance": {
            "ytd": 30.0,
            "oneYear": 150.0,
            "threeYear": 600.0,
            "fiveYear": 1000.0
        }
    }
]

# Sample investment recommendations
INVESTMENT_RECOMMENDATIONS = [
    {
        "recommendationId": "R1001",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "date": "2024-03-20",
        "type": "Portfolio Rebalancing",
        "description": "Consider rebalancing portfolio to maintain target allocation",
        "priority": "High",
        "details": {
            "currentAllocation": {
                "stocks": 65,
                "bonds": 25,
                "cash": 10
            },
            "targetAllocation": {
                "stocks": 60,
                "bonds": 30,
                "cash": 10
            },
            "recommendedActions": [
                "Reduce stock exposure by 5%",
                "Increase bond allocation by 5%"
            ]
        }
    },
    {
        "recommendationId": "R2001",
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "date": "2024-03-20",
        "type": "New Investment",
        "description": "Consider adding international exposure",
        "priority": "Medium",
        "details": {
            "recommendedInvestment": "VXUS",
            "suggestedAmount": 100000.00,
            "rationale": "Diversification and growth potential in emerging markets"
        }
    },
    {
        "recommendationId": "R3001",
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "date": "2024-03-20",
        "type": "Risk Assessment",
        "description": "Review risk tolerance and adjust portfolio accordingly",
        "priority": "Medium",
        "details": {
            "currentRiskScore": 7,
            "recommendedRiskScore": 6,
            "suggestedChanges": [
                "Increase bond allocation",
                "Add more defensive stocks"
            ]
        }
    },
    {
        "recommendationId": "R4001",
        "userId": "U4001",
        "userName": "Gary Player",
        "date": "2024-03-20",
        "type": "Dividend Strategy",
        "description": "Optimize dividend yield strategy",
        "priority": "High",
        "details": {
            "currentYield": 2.5,
            "targetYield": 3.0,
            "recommendedActions": [
                "Increase allocation to high-dividend stocks",
                "Consider dividend-focused ETFs"
            ]
        }
    },
    {
        "recommendationId": "R5001",
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "date": "2024-03-20",
        "type": "Tax Optimization",
        "description": "Implement tax-loss harvesting strategy",
        "priority": "High",
        "details": {
            "currentTaxEfficiency": 85,
            "targetTaxEfficiency": 95,
            "recommendedActions": [
                "Harvest losses in underperforming positions",
                "Consider tax-exempt municipal bonds"
            ]
        }
    },
    {
        "recommendationId": "R6001",
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "date": "2024-03-20",
        "type": "Estate Planning",
        "description": "Review trust and estate planning strategies",
        "priority": "High",
        "details": {
            "currentEstateValue": 4200000.00,
            "recommendedActions": [
                "Update trust documents",
                "Consider charitable giving strategies"
            ]
        }
    },
    {
        "recommendationId": "R7001",
        "userId": "U7001",
        "userName": "Greg Norman",
        "date": "2024-03-20",
        "type": "Business Expansion",
        "description": "Align investment strategy with business goals",
        "priority": "High",
        "details": {
            "businessGoals": [
                "Expand golf course portfolio",
                "Develop new product lines"
            ],
            "recommendedActions": [
                "Increase allocation to real estate investments",
                "Consider private equity opportunities"
            ]
        }
    }
]

# Sample market analysis
MARKET_ANALYSIS = {
    "date": "2024-03-20",
    "marketIndices": {
        "S&P 500": {
            "value": 4500.00,
            "change": 1.2,
            "ytd": 8.5
        },
        "Dow Jones": {
            "value": 35000.00,
            "change": 0.8,
            "ytd": 7.2
        },
        "NASDAQ": {
            "value": 15000.00,
            "change": 1.5,
            "ytd": 9.8
        }
    },
    "sectorPerformance": {
        "Technology": 2.5,
        "Healthcare": 1.2,
        "Financials": 0.8,
        "Consumer": 1.5,
        "Energy": -0.5
    },
    "marketSentiment": "Bullish",
    "keyEvents": [
        {
            "date": "2024-03-20",
            "description": "Fed maintains interest rates",
            "impact": "Positive"
        },
        {
            "date": "2024-03-19",
            "description": "Strong retail sales data",
            "impact": "Positive"
        }
    ]
}

@tool
def get_investment_portfolios(userId: str = None, userName: str = None):
    """
    Retrieve detailed information about investment portfolios for a specific user (if provided), including holdings, performance metrics, and rebalancing history.

    :param userId: (optional) Unique identifier for the investor (matches 'userId' in the data)
    :param userName: (optional) Name of the investor (matches 'userName' in the data)
    :returns: A list of dictionaries, each containing details about a specific portfolio:
              - 'portfolioId': Unique identifier for the portfolio
              - 'userId': Unique identifier for the investor
              - 'userName': Name of the investor
              - 'portfolioName': Name of the portfolio
              - 'totalValue': Total portfolio value
              - 'riskProfile': Risk profile of the portfolio
              - 'investmentGoal': Investment goal
              - 'targetDate': Target date for the investment goal
              - 'lastUpdated': Last update date
              - 'holdings': List of investment holdings
              - 'performance': Portfolio performance metrics
    """
    results = INVESTMENT_PORTFOLIOS
    if userId:
        results = [p for p in results if p["userId"] == userId]
    if userName:
        results = [p for p in results if p["userName"].lower() == userName.lower()]
    return results

@tool
def get_investment_recommendations(userId: str = None, userName: str = None):
    """
    Retrieve personalized investment recommendations for a specific user (if provided) based on portfolio analysis and market conditions.

    :param userId: (optional) Unique identifier for the investor (matches 'userId' in the data)
    :param userName: (optional) Name of the investor (matches 'userName' in the data)
    :returns: A list of dictionaries, each containing details about a specific recommendation:
              - 'recommendationId': Unique identifier for the recommendation
              - 'userId': Unique identifier for the investor
              - 'userName': Name of the investor
              - 'date': Date of the recommendation
              - 'type': Type of recommendation
              - 'description': Description of the recommendation
              - 'priority': Priority level of the recommendation
              - 'details': Detailed information about the recommendation
    """
    results = INVESTMENT_RECOMMENDATIONS
    if userId:
        results = [r for r in results if r["userId"] == userId]
    if userName:
        results = [r for r in results if r["userName"].lower() == userName.lower()]
    return results

@tool
def get_market_analysis():
    """
    Retrieve current market analysis including market indices, sector performance,
    and key market events.

    :returns: A dictionary containing market analysis information:
              - 'date': Date of the analysis
              - 'marketIndices': Dictionary of major market indices
              - 'sectorPerformance': Dictionary of sector performance
              - 'marketSentiment': Current market sentiment
              - 'keyEvents': List of key market events
    """
    return MARKET_ANALYSIS

@tool
def get_investment_opportunities(risk_profile: str = None, investment_amount: float = None):
    """
    Retrieve investment opportunities based on risk profile and investment amount.

    :param risk_profile: Optional risk profile filter (Conservative, Moderate, Aggressive)
    :param investment_amount: Optional minimum investment amount
    :returns: A list of dictionaries containing investment opportunities:
              - 'symbol': Investment symbol
              - 'name': Investment name
              - 'type': Investment type
              - 'riskLevel': Risk level
              - 'expectedReturn': Expected return
              - 'minimumInvestment': Minimum investment amount
              - 'description': Investment description
    """
    opportunities = [
        {
            "symbol": "VTI",
            "name": "Vanguard Total Stock Market ETF",
            "type": "ETF",
            "riskLevel": "Moderate",
            "expectedReturn": 10.5,
            "minimumInvestment": 1000.00,
            "description": "Broad market exposure with low expense ratio"
        },
        {
            "symbol": "VWO",
            "name": "Vanguard FTSE Emerging Markets ETF",
            "type": "ETF",
            "riskLevel": "High",
            "expectedReturn": 12.5,
            "minimumInvestment": 1000.00,
            "description": "Exposure to emerging markets"
        },
        {
            "symbol": "BND",
            "name": "Vanguard Total Bond Market ETF",
            "type": "ETF",
            "riskLevel": "Conservative",
            "expectedReturn": 4.5,
            "minimumInvestment": 1000.00,
            "description": "Broad bond market exposure"
        }
    ]
    
    if risk_profile:
        opportunities = [o for o in opportunities if o["riskLevel"] == risk_profile]
    if investment_amount:
        opportunities = [o for o in opportunities if o["minimumInvestment"] <= investment_amount]
    
    return opportunities 