from Stock import Stock

class GlobalMarket:
    def __init__(self):
        self.stocks = []
        self.funds = []
        self.commodities = []
        self.marketCap = 0

    def getGlobalMarketValue(self):
        '''return the total net worth of stocks,funds and comm'''
        total = 0
        for S in self.stocks:
            pass


