

class StockCalculator(object):
    """"StockCalculator calculates the highest maximum profit for a given list
    of historic stock prices.
    """
    def __init__(self, stock_prices):
        self.stock_prices = stock_prices

    def get_max_profit(self):
        """Calculates the maximum profit from `stock_prices`.
        """
        max_profit = 0

        # for each stock price, let's check if it provides a higher maximum
        # profit compared with all stock ticks in the future.
        for i, current_price in enumerate(self.stock_prices):

            # i+1: takes a slice of all stocks after the current time.
            # this ensures that all stocks are purchased before selling.
            for later_price in self.stock_prices[i+1:]:
                potential_profit = later_price - current_price

                # only increases if the it's greater than the previous value.
                max_profit = max(max_profit, potential_profit)

        return max_profit
