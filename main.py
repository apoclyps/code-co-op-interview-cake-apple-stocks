"""
InterviewCake - Apple Stocks
"""
from stocks.stock_calculator import StockCalculator

if __name__ == "__main__":
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    calculator = StockCalculator(stock_prices_yesterday)
    max_profit = calculator.get_max_profit()

    print(max_profit)
