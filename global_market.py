from stock import Stock

''' global_market.py '''
class GlobalMarket(object):
    ''' global market object'''
    def __init__(self):
        self.stocks = []
        self.funds = []
        self.commodities = []
        self.market_cap = 0
        self.optimism = 1.0

    def get_global_market_value(self):
        '''return the total net worth of stocks,funds and comm'''
        total = 0
        for S in self.stocks:
            total += (S.get_shares() * S.get_price())
        return total

    def get_global_market_stocks(self):
        ''' return a list of stocks '''
        return self.stocks

    def add_stock(self, new_stock):
        ''' Add a Stock to the GM '''
        self.stocks.append(new_stock)

    def tick(self):
        ''' update all global_market stuff to simulate activity '''
        # stocks

        # funds

        # commodities



