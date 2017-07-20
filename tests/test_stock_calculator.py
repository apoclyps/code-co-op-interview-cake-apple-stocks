import unittest

from stocks.stock_calculator import StockCalculator


class StockCalculatorTest(unittest.TestCase):
    def test_empty_stocks(self):
        stock_prices_yesterday = []
        calculator = StockCalculator(stock_prices_yesterday)
        max_profit = calculator.get_max_profit()

        self.assertEqual(max_profit, 0)

    def test_0_precent_profit(self):
        stock_prices_yesterday = [0, 0, 0, 0]
        calculator = StockCalculator(stock_prices_yesterday)
        max_profit = calculator.get_max_profit()

        self.assertEqual(max_profit, 0)

    def test_max_profit(self):
        stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        calculator = StockCalculator(stock_prices_yesterday)
        max_profit = calculator.get_max_profit()

        self.assertEqual(max_profit, 6)

    def test_max_profit_high_yield(self):
        stock_prices_yesterday = [10, 50, 20, 90, 20, 1000]
        calculator = StockCalculator(stock_prices_yesterday)
        max_profit = calculator.get_max_profit()

        self.assertEqual(max_profit, 990)

    def test_100_precent_profit(self):
        stock_prices_yesterday = [0, 50, 20, 90, 20, 1000]
        calculator = StockCalculator(stock_prices_yesterday)
        max_profit = calculator.get_max_profit()

        self.assertEqual(max_profit, 1000)
