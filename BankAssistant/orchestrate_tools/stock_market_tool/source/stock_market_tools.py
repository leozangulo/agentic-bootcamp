from ibm_watsonx_orchestrate.agent_builder.tools import tool
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

@tool
def get_stock_info(symbol: str):
    """
    Retrieve current information about a specific stock.

    :param symbol: Stock symbol (e.g., 'AAPL' for Apple)
    :returns: A dictionary containing stock information:
              - 'symbol': Stock symbol
              - 'name': Company name
              - 'currentPrice': Current stock price
              - 'previousClose': Previous closing price
              - 'open': Opening price
              - 'dayHigh': Day's high price
              - 'dayLow': Day's low price
              - 'volume': Trading volume
              - 'marketCap': Market capitalization
              - 'fiftyTwoWeekHigh': 52-week high
              - 'fiftyTwoWeekLow': 52-week low
              - 'dividendYield': Dividend yield
              - 'peRatio': Price/Earnings ratio
    """
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        
        return {
            "symbol": symbol,
            "name": info.get('longName', 'N/A'),
            "currentPrice": info.get('currentPrice', 'N/A'),
            "previousClose": info.get('previousClose', 'N/A'),
            "open": info.get('open', 'N/A'),
            "dayHigh": info.get('dayHigh', 'N/A'),
            "dayLow": info.get('dayLow', 'N/A'),
            "volume": info.get('volume', 'N/A'),
            "marketCap": info.get('marketCap', 'N/A'),
            "fiftyTwoWeekHigh": info.get('fiftyTwoWeekHigh', 'N/A'),
            "fiftyTwoWeekLow": info.get('fiftyTwoWeekLow', 'N/A'),
            "dividendYield": info.get('dividendYield', 'N/A'),
            "peRatio": info.get('trailingPE', 'N/A')
        }
    except Exception as e:
        return {"error": f"Failed to fetch stock information: {str(e)}"}

@tool
def get_stock_history(symbol: str, period: str = "1mo", interval: str = "1d"):
    """
    Retrieve historical stock data for a specific symbol.

    :param symbol: Stock symbol (e.g., 'AAPL' for Apple)
    :param period: Time period to fetch (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
    :param interval: Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
    :returns: A dictionary containing historical data:
              - 'symbol': Stock symbol
              - 'period': Time period
              - 'interval': Data interval
              - 'data': List of daily data points
              - 'summary': Summary statistics
    """
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period, interval=interval)
        
        # Convert DataFrame to list of dictionaries
        data = []
        for index, row in hist.iterrows():
            data.append({
                "date": index.strftime("%Y-%m-%d"),
                "open": row['Open'],
                "high": row['High'],
                "low": row['Low'],
                "close": row['Close'],
                "volume": row['Volume']
            })
        
        # Calculate summary statistics
        summary = {
            "startPrice": hist['Close'].iloc[0],
            "endPrice": hist['Close'].iloc[-1],
            "highPrice": hist['High'].max(),
            "lowPrice": hist['Low'].min(),
            "averageVolume": hist['Volume'].mean(),
            "priceChange": hist['Close'].iloc[-1] - hist['Close'].iloc[0],
            "percentChange": ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
        }
        
        return {
            "symbol": symbol,
            "period": period,
            "interval": interval,
            "data": data,
            "summary": summary
        }
    except Exception as e:
        return {"error": f"Failed to fetch stock history: {str(e)}"}

@tool
def get_stock_recommendations(symbol: str):
    """
    Retrieve analyst recommendations for a specific stock.

    :param symbol: Stock symbol (e.g., 'AAPL' for Apple)
    :returns: A dictionary containing recommendation information:
              - 'symbol': Stock symbol
              - 'recommendations': List of recent recommendations
              - 'summary': Summary of recommendations
    """
    try:
        stock = yf.Ticker(symbol)
        recommendations = stock.recommendations
        
        if recommendations is None or recommendations.empty:
            return {"error": "No recommendations available"}
        
        # Convert DataFrame to list of dictionaries
        recs = []
        for index, row in recommendations.iterrows():
            recs.append({
                "date": index.strftime("%Y-%m-%d"),
                "firm": row['Firm'],
                "recommendation": row['To Grade'],
                "action": row['Action']
            })
        
        # Calculate recommendation summary
        summary = {
            "totalRecommendations": len(recs),
            "latestRecommendation": recs[0] if recs else None,
            "recommendationBreakdown": recommendations['To Grade'].value_counts().to_dict()
        }
        
        return {
            "symbol": symbol,
            "recommendations": recs,
            "summary": summary
        }
    except Exception as e:
        return {"error": f"Failed to fetch stock recommendations: {str(e)}"}

@tool
def get_market_summary():
    """
    Retrieve summary information for major market indices.

    :returns: A dictionary containing market summary information:
              - 'date': Current date
              - 'indices': Dictionary of major indices
              - 'summary': Market summary statistics
    """
    try:
        # Major market indices
        indices = {
            "^GSPC": "S&P 500",
            "^DJI": "Dow Jones",
            "^IXIC": "NASDAQ",
            "^RUT": "Russell 2000"
        }
        
        market_data = {}
        for symbol, name in indices.items():
            ticker = yf.Ticker(symbol)
            info = ticker.info
            
            market_data[name] = {
                "symbol": symbol,
                "value": info.get('regularMarketPrice', 'N/A'),
                "change": info.get('regularMarketChange', 'N/A'),
                "percentChange": info.get('regularMarketChangePercent', 'N/A'),
                "volume": info.get('regularMarketVolume', 'N/A')
            }
        
        # Calculate market summary
        summary = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "marketStatus": "Open" if datetime.now().hour < 16 else "Closed",
            "advancingStocks": "N/A",  # Would require additional API calls
            "decliningStocks": "N/A",  # Would require additional API calls
            "marketBreadth": "N/A"     # Would require additional API calls
        }
        
        return {
            "date": summary["date"],
            "indices": market_data,
            "summary": summary
        }
    except Exception as e:
        return {"error": f"Failed to fetch market summary: {str(e)}"}

@tool
def get_stock_news(symbol: str, limit: int = 5):
    """
    Retrieve recent news articles for a specific stock.

    :param symbol: Stock symbol (e.g., 'AAPL' for Apple)
    :param limit: Maximum number of news articles to return
    :returns: A dictionary containing news information:
              - 'symbol': Stock symbol
              - 'articles': List of news articles
    """
    try:
        stock = yf.Ticker(symbol)
        news = stock.news
        
        if not news:
            return {"error": "No news available"}
        
        articles = []
        for article in news[:limit]:
            articles.append({
                "title": article.get('title', 'N/A'),
                "publisher": article.get('publisher', 'N/A'),
                "link": article.get('link', 'N/A'),
                "published": datetime.fromtimestamp(article.get('providerPublishTime', 0)).strftime("%Y-%m-%d %H:%M:%S"),
                "type": article.get('type', 'N/A')
            })
        
        return {
            "symbol": symbol,
            "articles": articles
        }
    except Exception as e:
        return {"error": f"Failed to fetch stock news: {str(e)}"} 