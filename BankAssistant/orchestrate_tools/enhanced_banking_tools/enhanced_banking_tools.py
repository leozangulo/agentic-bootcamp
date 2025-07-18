from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import datetime, timedelta

# Static credit card data with consistent user IDs and billing addresses
CREDIT_CARDS = [
    # Arnold Palmer's Cards
    {
        "cardId": "CC1001",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "cardNumber": "4532-1234-5678-9012",
        "cardType": "Visa",
        "cardTier": "Platinum",
        "status": "Active",
        "creditLimit": 25000.00,
        "availableCredit": 18750.00,
        "currentBalance": 6250.00,
        "minimumPaymentDue": 250.00,
        "paymentDueDate": "2024-04-15",
        "lastPaymentDate": "2024-03-15",
        "lastPaymentAmount": 1250.00,
        "interestRate": 19.99,
        "rewardsRate": 2.5,
        "annualFee": 95.00,
        "issueDate": "2022-01-15",
        "expiryDate": "2026-01-15",
        "isContactless": True,
        "isInternationalEnabled": True,
        "dailyTransactionLimit": 5000.00,
        "cashAdvanceLimit": 2500.00,
        "cashAdvanceRate": 24.99,
        "latePaymentFee": 35.00,
        "overLimitFee": 35.00,
        "foreignTransactionFee": 2.5,
        "billingAddress": {
            "street": "123 Golf Club Drive",
            "city": "Orlando",
            "state": "FL",
            "zipCode": "32819",
            "country": "USA"
        }
    },
    # Jack Nicklaus's Cards
    {
        "cardId": "CC2001",
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "cardNumber": "3782-8224-6310-0055",
        "cardType": "American Express",
        "cardTier": "Signature",
        "status": "Active",
        "creditLimit": 50000.00,
        "availableCredit": 45000.00,
        "currentBalance": 5000.00,
        "minimumPaymentDue": 500.00,
        "paymentDueDate": "2024-04-10",
        "lastPaymentDate": "2024-03-10",
        "lastPaymentAmount": 2500.00,
        "interestRate": 18.99,
        "rewardsRate": 4.0,
        "annualFee": 550.00,
        "issueDate": "2021-03-15",
        "expiryDate": "2025-03-15",
        "isContactless": True,
        "isInternationalEnabled": True,
        "dailyTransactionLimit": 10000.00,
        "cashAdvanceLimit": 5000.00,
        "cashAdvanceRate": 24.99,
        "latePaymentFee": 40.00,
        "overLimitFee": 40.00,
        "foreignTransactionFee": 2.5,
        "billingAddress": {
            "street": "456 Golf Course Road",
            "city": "Jupiter",
            "state": "FL",
            "zipCode": "33478",
            "country": "USA"
        }
    },
    # Annika Sorenstam's Cards
    {
        "cardId": "CC3001",
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "cardNumber": "4532-7890-1234-5678",
        "cardType": "Visa",
        "cardTier": "Platinum",
        "status": "Active",
        "creditLimit": 30000.00,
        "availableCredit": 27000.00,
        "currentBalance": 3000.00,
        "minimumPaymentDue": 300.00,
        "paymentDueDate": "2024-04-20",
        "lastPaymentDate": "2024-03-20",
        "lastPaymentAmount": 1500.00,
        "interestRate": 19.99,
        "rewardsRate": 2.5,
        "annualFee": 95.00,
        "issueDate": "2022-06-01",
        "expiryDate": "2026-06-01",
        "isContactless": True,
        "isInternationalEnabled": True,
        "dailyTransactionLimit": 6000.00,
        "cashAdvanceLimit": 3000.00,
        "cashAdvanceRate": 24.99,
        "latePaymentFee": 35.00,
        "overLimitFee": 35.00,
        "foreignTransactionFee": 2.5,
        "billingAddress": {
            "street": "789 Golf Club Lane",
            "city": "Orlando",
            "state": "FL",
            "zipCode": "32819",
            "country": "USA"
        }
    },
    # Gary Player's Cards
    {
        "cardId": "CC4001",
        "userId": "U4001",
        "userName": "Gary Player",
        "cardNumber": "5421-9876-5432-1098",
        "cardType": "Mastercard",
        "cardTier": "World Elite",
        "status": "Active",
        "creditLimit": 75000.00,
        "availableCredit": 67500.00,
        "currentBalance": 7500.00,
        "minimumPaymentDue": 750.00,
        "paymentDueDate": "2024-04-05",
        "lastPaymentDate": "2024-03-05",
        "lastPaymentAmount": 3750.00,
        "interestRate": 18.99,
        "rewardsRate": 3.0,
        "annualFee": 195.00,
        "issueDate": "2021-09-15",
        "expiryDate": "2025-09-15",
        "isContactless": True,
        "isInternationalEnabled": True,
        "dailyTransactionLimit": 15000.00,
        "cashAdvanceLimit": 7500.00,
        "cashAdvanceRate": 24.99,
        "latePaymentFee": 40.00,
        "overLimitFee": 40.00,
        "foreignTransactionFee": 2.5,
        "billingAddress": {
            "street": "321 Golf Estate Drive",
            "city": "Jupiter",
            "state": "FL",
            "zipCode": "33478",
            "country": "USA"
        }
    },
    # Phil Mickelson's Cards
    {
        "cardId": "CC5001",
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "cardNumber": "3782-8224-6310-0056",
        "cardType": "American Express",
        "cardTier": "Centurion",
        "status": "Active",
        "creditLimit": 100000.00,
        "availableCredit": 90000.00,
        "currentBalance": 10000.00,
        "minimumPaymentDue": 1000.00,
        "paymentDueDate": "2024-04-15",
        "lastPaymentDate": "2024-03-15",
        "lastPaymentAmount": 5000.00,
        "interestRate": 17.99,
        "rewardsRate": 5.0,
        "annualFee": 2500.00,
        "issueDate": "2020-12-01",
        "expiryDate": "2024-12-01",
        "isContactless": True,
        "isInternationalEnabled": True,
        "dailyTransactionLimit": 20000.00,
        "cashAdvanceLimit": 10000.00,
        "cashAdvanceRate": 24.99,
        "latePaymentFee": 50.00,
        "overLimitFee": 50.00,
        "foreignTransactionFee": 2.5,
        "billingAddress": {
            "street": "555 Golf Resort Way",
            "city": "Rancho Santa Fe",
            "state": "CA",
            "zipCode": "92067",
            "country": "USA"
        }
    },
    # Seve Ballesteros's Cards
    {
        "cardId": "CC6001",
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "cardNumber": "4532-1111-2222-3333",
        "cardType": "Visa",
        "cardTier": "Infinite",
        "status": "Active",
        "creditLimit": 60000.00,
        "availableCredit": 54000.00,
        "currentBalance": 6000.00,
        "minimumPaymentDue": 600.00,
        "paymentDueDate": "2024-04-10",
        "lastPaymentDate": "2024-03-10",
        "lastPaymentAmount": 3000.00,
        "interestRate": 18.99,
        "rewardsRate": 3.5,
        "annualFee": 495.00,
        "issueDate": "2021-06-15",
        "expiryDate": "2025-06-15",
        "isContactless": True,
        "isInternationalEnabled": True,
        "dailyTransactionLimit": 12000.00,
        "cashAdvanceLimit": 6000.00,
        "cashAdvanceRate": 24.99,
        "latePaymentFee": 40.00,
        "overLimitFee": 40.00,
        "foreignTransactionFee": 2.5,
        "billingAddress": {
            "street": "888 Golf Villa Court",
            "city": "Miami",
            "state": "FL",
            "zipCode": "33139",
            "country": "USA"
        }
    },
    # Greg Norman's Cards
    {
        "cardId": "CC7001",
        "userId": "U7001",
        "userName": "Greg Norman",
        "cardNumber": "5421-4444-5555-6666",
        "cardType": "Mastercard",
        "cardTier": "World Elite",
        "status": "Active",
        "creditLimit": 85000.00,
        "availableCredit": 76500.00,
        "currentBalance": 8500.00,
        "minimumPaymentDue": 850.00,
        "paymentDueDate": "2024-04-20",
        "lastPaymentDate": "2024-03-20",
        "lastPaymentAmount": 4250.00,
        "interestRate": 18.99,
        "rewardsRate": 3.0,
        "annualFee": 195.00,
        "issueDate": "2021-03-01",
        "expiryDate": "2025-03-01",
        "isContactless": True,
        "isInternationalEnabled": True,
        "dailyTransactionLimit": 17000.00,
        "cashAdvanceLimit": 8500.00,
        "cashAdvanceRate": 24.99,
        "latePaymentFee": 40.00,
        "overLimitFee": 40.00,
        "foreignTransactionFee": 2.5,
        "billingAddress": {
            "street": "777 Golf Business Park",
            "city": "West Palm Beach",
            "state": "FL",
            "zipCode": "33401",
            "country": "USA"
        }
    },
    # Tiger Woods's Cards
    {
        "cardId": "CC8001",
        "userId": "U8001",
        "userName": "Tiger Woods",
        "cardNumber": "5421-7777-8888-9999",
        "cardType": "Mastercard",
        "cardTier": "World Elite",
        "status": "Active",
        "creditLimit": 120000.00,
        "availableCredit": 110000.00,
        "currentBalance": 10000.00,
        "minimumPaymentDue": 1000.00,
        "paymentDueDate": "2024-04-15",
        "lastPaymentDate": "2024-03-15",
        "lastPaymentAmount": 4000.00,
        "interestRate": 17.99,
        "rewardsRate": 4.0,
        "annualFee": 295.00,
        "issueDate": "2020-03-15",
        "expiryDate": "2024-03-15",
        "isContactless": True,
        "isInternationalEnabled": True,
        "dailyTransactionLimit": 25000.00,
        "cashAdvanceLimit": 12500.00,
        "cashAdvanceRate": 24.99,
        "latePaymentFee": 50.00,
        "overLimitFee": 50.00,
        "foreignTransactionFee": 2.5,
        "billingAddress": {
            "street": "1000 Augusta Drive",
            "city": "Augusta",
            "state": "GA",
            "zipCode": "30904",
            "country": "USA"
        }
    }
]

# Static loyalty data with matching user IDs
LOYALTY_DATA = [
    {
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "membershipTier": "Platinum",
        "status": "Active",
        "totalPoints": 750000,
        "availablePoints": 500000,
        "pointsExpiringThisMonth": 25000,
        "lifetimePointsEarned": 1500000,
        "lifetimePointsRedeemed": 750000,
        "membershipStartDate": "2020-01-15",
        "lastActivityDate": "2024-03-20",
        "preferredRewards": {
            "travel": 80,
            "merchandise": 40,
            "cashback": 60,
            "giftCards": 20
        },
        "specialOffers": [
            {
                "offerId": "OFF1001",
                "description": "Special Travel offer - 3x points on all travel purchases",
                "validUntil": "2024-04-30",
                "pointsMultiplier": 3.0
            }
        ]
    },
    {
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "membershipTier": "Diamond",
        "status": "Active",
        "totalPoints": 1200000,
        "availablePoints": 800000,
        "pointsExpiringThisMonth": 0,
        "lifetimePointsEarned": 2500000,
        "lifetimePointsRedeemed": 1300000,
        "membershipStartDate": "2019-03-15",
        "lastActivityDate": "2024-03-15",
        "preferredRewards": {
            "travel": 90,
            "merchandise": 30,
            "cashback": 40,
            "giftCards": 10
        },
        "specialOffers": [
            {
                "offerId": "OFF2001",
                "description": "Luxury Travel Package - 50% off points redemption",
                "validUntil": "2024-06-30",
                "pointsMultiplier": 1.5
            }
        ]
    },
    {
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "membershipTier": "Platinum",
        "status": "Active",
        "totalPoints": 600000,
        "availablePoints": 400000,
        "pointsExpiringThisMonth": 20000,
        "lifetimePointsEarned": 1200000,
        "lifetimePointsRedeemed": 600000,
        "membershipStartDate": "2021-06-01",
        "lastActivityDate": "2024-03-20",
        "preferredRewards": {
            "travel": 70,
            "merchandise": 50,
            "cashback": 50,
            "giftCards": 30
        },
        "specialOffers": [
            {
                "offerId": "OFF3001",
                "description": "Golf Equipment Bonus - 2x points on golf purchases",
                "validUntil": "2024-05-15",
                "pointsMultiplier": 2.0
            }
        ]
    },
    {
        "userId": "U4001",
        "userName": "Gary Player",
        "membershipTier": "Diamond",
        "status": "Active",
        "totalPoints": 1500000,
        "availablePoints": 1000000,
        "pointsExpiringThisMonth": 0,
        "lifetimePointsEarned": 3000000,
        "lifetimePointsRedeemed": 1500000,
        "membershipStartDate": "2018-09-15",
        "lastActivityDate": "2024-03-05",
        "preferredRewards": {
            "travel": 85,
            "merchandise": 35,
            "cashback": 45,
            "giftCards": 15
        },
        "specialOffers": [
            {
                "offerId": "OFF4001",
                "description": "Business Travel Bonus - 4x points on business travel",
                "validUntil": "2024-07-31",
                "pointsMultiplier": 4.0
            }
        ]
    },
    {
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "membershipTier": "Diamond",
        "status": "Active",
        "totalPoints": 2000000,
        "availablePoints": 1500000,
        "pointsExpiringThisMonth": 0,
        "lifetimePointsEarned": 4000000,
        "lifetimePointsRedeemed": 2000000,
        "membershipStartDate": "2017-12-01",
        "lastActivityDate": "2024-03-15",
        "preferredRewards": {
            "travel": 95,
            "merchandise": 25,
            "cashback": 35,
            "giftCards": 5
        },
        "specialOffers": [
            {
                "offerId": "OFF5001",
                "description": "Private Jet Travel - 5x points on private jet bookings",
                "validUntil": "2024-08-31",
                "pointsMultiplier": 5.0
            }
        ]
    },
    {
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "membershipTier": "Platinum",
        "status": "Active",
        "totalPoints": 900000,
        "availablePoints": 600000,
        "pointsExpiringThisMonth": 30000,
        "lifetimePointsEarned": 1800000,
        "lifetimePointsRedeemed": 900000,
        "membershipStartDate": "2020-06-15",
        "lastActivityDate": "2024-03-10",
        "preferredRewards": {
            "travel": 75,
            "merchandise": 45,
            "cashback": 55,
            "giftCards": 25
        },
        "specialOffers": [
            {
                "offerId": "OFF6001",
                "description": "Family Travel Package - 3x points on family vacations",
                "validUntil": "2024-09-30",
                "pointsMultiplier": 3.0
            }
        ]
    },
    {
        "userId": "U7001",
        "userName": "Greg Norman",
        "membershipTier": "Diamond",
        "status": "Active",
        "totalPoints": 1800000,
        "availablePoints": 1200000,
        "pointsExpiringThisMonth": 0,
        "lifetimePointsEarned": 3600000,
        "lifetimePointsRedeemed": 1800000,
        "membershipStartDate": "2019-03-01",
        "lastActivityDate": "2024-03-20",
        "preferredRewards": {
            "travel": 90,
            "merchandise": 30,
            "cashback": 40,
            "giftCards": 10
        },
        "specialOffers": [
            {
                "offerId": "OFF7001",
                "description": "Business Expansion Bonus - 4x points on business expenses",
                "validUntil": "2024-10-31",
                "pointsMultiplier": 4.0
            }
        ]
    }
]

# Static transaction history data
TRANSACTION_HISTORY = [
    # Arnold Palmer's transactions
    {
        "transactionId": "TRX1001",
        "cardId": "CC1001",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "date": "2024-03-15",
        "amount": 1250.00,
        "description": "Golf Club Equipment Purchase",
        "category": "Sports",
        "merchantName": "PGA Tour Superstore",
        "merchantCategory": "Sporting Goods",
        "location": {
            "city": "Orlando",
            "state": "FL",
            "country": "USA"
        },
        "status": "Completed",
        "rewardsEarned": 2500,
        "isInternational": False,
        "isRecurring": False
    },
    # Jack Nicklaus's transactions
    {
        "transactionId": "TRX2001",
        "cardId": "CC2001",
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "date": "2024-03-10",
        "amount": 2500.00,
        "description": "Private Jet Charter",
        "category": "Travel",
        "merchantName": "NetJets",
        "merchantCategory": "Air Travel",
        "location": {
            "city": "Jupiter",
            "state": "FL",
            "country": "USA"
        },
        "status": "Completed",
        "rewardsEarned": 5000,
        "isInternational": False,
        "isRecurring": False
    },
    # Annika Sorenstam's transactions
    {
        "transactionId": "TRX3001",
        "cardId": "CC3001",
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "date": "2024-03-20",
        "amount": 1500.00,
        "description": "Golf Tournament Entry",
        "category": "Entertainment",
        "merchantName": "LPGA Tour",
        "merchantCategory": "Event",
        "location": {
            "city": "Orlando",
            "state": "FL",
            "country": "USA"
        },
        "status": "Completed",
        "rewardsEarned": 3000,
        "isInternational": False,
        "isRecurring": False
    },
    # Gary Player's transactions
    {
        "transactionId": "TRX4001",
        "cardId": "CC4001",
        "userId": "U4001",
        "userName": "Gary Player",
        "date": "2024-03-05",
        "amount": 3750.00,
        "description": "Business Meeting Expenses",
        "category": "Business",
        "merchantName": "The Ritz-Carlton",
        "merchantCategory": "Hotel",
        "location": {
            "city": "Jupiter",
            "state": "FL",
            "country": "USA"
        },
        "status": "Completed",
        "rewardsEarned": 7500,
        "isInternational": False,
        "isRecurring": False
    },
    # Phil Mickelson's transactions
    {
        "transactionId": "TRX5001",
        "cardId": "CC5001",
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "date": "2024-03-15",
        "amount": 5000.00,
        "description": "Private Jet Charter",
        "category": "Travel",
        "merchantName": "Wheels Up",
        "merchantCategory": "Air Travel",
        "location": {
            "city": "Rancho Santa Fe",
            "state": "CA",
            "country": "USA"
        },
        "status": "Completed",
        "rewardsEarned": 10000,
        "isInternational": False,
        "isRecurring": False
    },
    # Seve Ballesteros's transactions
    {
        "transactionId": "TRX6001",
        "cardId": "CC6001",
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "date": "2024-03-10",
        "amount": 3000.00,
        "description": "Family Vacation Booking",
        "category": "Travel",
        "merchantName": "Four Seasons",
        "merchantCategory": "Hotel",
        "location": {
            "city": "Miami",
            "state": "FL",
            "country": "USA"
        },
        "status": "Completed",
        "rewardsEarned": 6000,
        "isInternational": False,
        "isRecurring": False
    },
    # Greg Norman's transactions
    {
        "transactionId": "TRX7001",
        "cardId": "CC7001",
        "userId": "U7001",
        "userName": "Greg Norman",
        "date": "2024-03-20",
        "amount": 4250.00,
        "description": "Business Expansion Meeting",
        "category": "Business",
        "merchantName": "The Breakers",
        "merchantCategory": "Hotel",
        "location": {
            "city": "West Palm Beach",
            "state": "FL",
            "country": "USA"
        },
        "status": "Completed",
        "rewardsEarned": 8500,
        "isInternational": False,
        "isRecurring": False
    }
]

# Static bill payment history
BILL_PAYMENT_HISTORY = [
    # Arnold Palmer's payments
    {
        "paymentId": "PAY1001",
        "cardId": "CC1001",
        "userId": "U1001",
        "userName": "Arnold Palmer",
        "date": "2024-03-15",
        "amount": 1250.00,
        "paymentMethod": "Bank Transfer",
        "status": "Completed",
        "description": "Monthly Payment",
        "billingCycle": "2024-03",
        "lateFee": 0.00,
        "interestCharged": 0.00
    },
    # Jack Nicklaus's payments
    {
        "paymentId": "PAY2001",
        "cardId": "CC2001",
        "userId": "U2001",
        "userName": "Jack Nicklaus",
        "date": "2024-03-10",
        "amount": 2500.00,
        "paymentMethod": "Bank Transfer",
        "status": "Completed",
        "description": "Monthly Payment",
        "billingCycle": "2024-03",
        "lateFee": 0.00,
        "interestCharged": 0.00
    },
    # Annika Sorenstam's payments
    {
        "paymentId": "PAY3001",
        "cardId": "CC3001",
        "userId": "U3001",
        "userName": "Annika Sorenstam",
        "date": "2024-03-20",
        "amount": 1500.00,
        "paymentMethod": "Bank Transfer",
        "status": "Completed",
        "description": "Monthly Payment",
        "billingCycle": "2024-03",
        "lateFee": 0.00,
        "interestCharged": 0.00
    },
    # Gary Player's payments
    {
        "paymentId": "PAY4001",
        "cardId": "CC4001",
        "userId": "U4001",
        "userName": "Gary Player",
        "date": "2024-03-05",
        "amount": 3750.00,
        "paymentMethod": "Bank Transfer",
        "status": "Completed",
        "description": "Monthly Payment",
        "billingCycle": "2024-03",
        "lateFee": 0.00,
        "interestCharged": 0.00
    },
    # Phil Mickelson's payments
    {
        "paymentId": "PAY5001",
        "cardId": "CC5001",
        "userId": "U5001",
        "userName": "Phil Mickelson",
        "date": "2024-03-15",
        "amount": 5000.00,
        "paymentMethod": "Bank Transfer",
        "status": "Completed",
        "description": "Monthly Payment",
        "billingCycle": "2024-03",
        "lateFee": 0.00,
        "interestCharged": 0.00
    },
    # Seve Ballesteros's payments
    {
        "paymentId": "PAY6001",
        "cardId": "CC6001",
        "userId": "U6001",
        "userName": "Seve Ballesteros",
        "date": "2024-03-10",
        "amount": 3000.00,
        "paymentMethod": "Bank Transfer",
        "status": "Completed",
        "description": "Monthly Payment",
        "billingCycle": "2024-03",
        "lateFee": 0.00,
        "interestCharged": 0.00
    },
    # Greg Norman's payments
    {
        "paymentId": "PAY7001",
        "cardId": "CC7001",
        "userId": "U7001",
        "userName": "Greg Norman",
        "date": "2024-03-20",
        "amount": 4250.00,
        "paymentMethod": "Bank Transfer",
        "status": "Completed",
        "description": "Monthly Payment",
        "billingCycle": "2024-03",
        "lateFee": 0.00,
        "interestCharged": 0.00
    }
]

@tool
def get_enhanced_credit_cards(userId: str = None, userName: str = None):
    """
    Retrieve detailed information about credit cards for a specific user (if provided).

    :param userId: (optional) Unique identifier for the cardholder (matches 'userId' in the data)
    :param userName: (optional) Name of the cardholder (matches 'userName' in the data)
    :returns: A list of dictionaries, each containing details about a specific credit card:
              - 'cardId': Unique identifier for the card
              - 'userId': Unique identifier for the cardholder
              - 'userName': Name of the cardholder
              - 'cardNumber': Masked credit card number
              - 'cardType': Type of card (Visa, Mastercard, etc.)
              - 'cardTier': Card tier (Standard, Gold, Platinum, etc.)
              - 'status': Current status of the card (Active, Expired, Disabled)
              - 'creditLimit': Total credit limit
              - 'availableCredit': Available credit
              - 'currentBalance': Current balance
              - 'minimumPaymentDue': Minimum payment amount
              - 'paymentDueDate': Due date for next payment
              - 'lastPaymentDate': Date of last payment
              - 'lastPaymentAmount': Amount of last payment
              - 'interestRate': Current interest rate
              - 'rewardsRate': Rewards earning rate
              - 'annualFee': Annual fee amount
              - 'issueDate': Card issue date
              - 'expiryDate': Card expiration date
              - 'isContactless': Whether card supports contactless payments
              - 'isInternationalEnabled': Whether international transactions are enabled
              - 'dailyTransactionLimit': Daily transaction limit
              - 'cashAdvanceLimit': Cash advance limit
              - 'cashAdvanceRate': Cash advance interest rate
              - 'latePaymentFee': Late payment fee amount
              - 'overLimitFee': Over limit fee amount
              - 'foreignTransactionFee': Foreign transaction fee percentage
              - 'billingAddress': Dictionary containing billing address details
    """
    if userId:
        return [card for card in CREDIT_CARDS if card["userId"] == userId]
    if userName:
        return [card for card in CREDIT_CARDS if card["userName"].lower() == userName.lower()]
    return CREDIT_CARDS

@tool
def get_enhanced_loyalty_info(userId: str = None, userName: str = None):
    """
    Retrieve detailed information about customer loyalty programs for a specific user (if provided), including points, membership status, and rewards preferences.

    :param userId: (optional) Unique identifier for the customer (matches 'userId' in the data)
    :param userName: (optional) Name of the customer (matches 'userName' in the data)
    :returns: A list of dictionaries, each containing details about a specific customer's loyalty program:
              - 'userId': Unique identifier for the customer
              - 'userName': Name of the customer
              - 'membershipTier': Current membership tier
              - 'status': Current membership status
              - 'totalPoints': Total points balance
              - 'availablePoints': Available points for redemption
              - 'pointsExpiringThisMonth': Points expiring in current month
              - 'lifetimePointsEarned': Total points earned
              - 'lifetimePointsRedeemed': Total points redeemed
              - 'membershipStartDate': Date when membership started
              - 'lastActivityDate': Date of last activity
              - 'preferredRewards': Dictionary of preferred reward categories
              - 'specialOffers': List of current special offers
              - 'recentTransactions': List of recent point transactions
              - 'upcomingMilestones': List of upcoming loyalty milestones
    """
    if userId:
        return [entry for entry in LOYALTY_DATA if entry["userId"] == userId]
    if userName:
        return [entry for entry in LOYALTY_DATA if entry["userName"].lower() == userName.lower()]
    return LOYALTY_DATA

@tool
def get_transaction_history(userId: str = None, userName: str = None, cardId: str = None):
    """
    Retrieve detailed transaction history for a specific user or card (if provided), including merchant information, location data, and rewards earned.

    :param userId: (optional) Unique identifier for the cardholder (matches 'userId' in the data)
    :param userName: (optional) Name of the cardholder (matches 'userName' in the data)
    :param cardId: (optional) Card identifier (matches 'cardId' in the data)
    :returns: A list of dictionaries, each containing details about a specific transaction:
              - 'transactionId': Unique identifier for the transaction
              - 'cardId': ID of the card used for the transaction
              - 'userId': ID of the cardholder
              - 'userName': Name of the cardholder
              - 'date': Transaction date
              - 'amount': Transaction amount
              - 'description': Transaction description
              - 'category': Transaction category
              - 'merchantName': Name of the merchant
              - 'merchantCategory': Category of the merchant
              - 'location': Dictionary containing location details
              - 'status': Transaction status
              - 'rewardsEarned': Points earned from the transaction
              - 'isInternational': Whether the transaction was international
              - 'isRecurring': Whether the transaction is recurring
    """
    results = TRANSACTION_HISTORY
    if userId:
        results = [t for t in results if t["userId"] == userId]
    if userName:
        results = [t for t in results if t["userName"].lower() == userName.lower()]
    if cardId:
        results = [t for t in results if t["cardId"] == cardId]
    return results

@tool
def get_bill_payment_history(userId: str = None, userName: str = None, cardId: str = None):
    """
    Retrieve detailed bill payment history for a specific user or card (if provided), including payment methods, status, and associated fees.

    :param userId: (optional) Unique identifier for the cardholder (matches 'userId' in the data)
    :param userName: (optional) Name of the cardholder (matches 'userName' in the data)
    :param cardId: (optional) Card identifier (matches 'cardId' in the data)
    :returns: A list of dictionaries, each containing details about a specific payment:
              - 'paymentId': Unique identifier for the payment
              - 'cardId': ID of the card the payment was made for
              - 'userId': ID of the cardholder
              - 'userName': Name of the cardholder
              - 'date': Payment date
              - 'amount': Payment amount
              - 'paymentMethod': Method used for payment
              - 'status': Payment status
              - 'description': Payment description
              - 'billingCycle': Billing cycle the payment was for
              - 'lateFee': Any late fees charged
              - 'interestCharged': Any interest charged
    """
    results = BILL_PAYMENT_HISTORY
    if userId:
        results = [p for p in results if p["userId"] == userId]
    if userName:
        results = [p for p in results if p["userName"].lower() == userName.lower()]
    if cardId:
        results = [p for p in results if p["cardId"] == cardId]
    return results 