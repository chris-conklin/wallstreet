''' WallStreet Stock module '''
class Stock(object):
    ''' creates a stock object '''
    def __init__(self, symbol, name, shares=0, price=0):
        self.symbol = symbol
        self.shares = shares
        self.price = price
        self.name = name


    def get_name(self):
        return self.name
        
    def set_name(self, newname):
        self.name = newname

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, newSymbol):
        self.symbol = newSymbol

    def get_price(self):
        return self.price

    def set_price(self, newamt):
        self.price = newamt

    def get_shares(self):
        return self.shares

    def set_shares(self, newamt):
        self.shares = newamt

    def add_shares(self, addition):
        self.shares += addition

    def sub_shares(self, deduction):
        self.shares -= deduction

    def get_value(self):
        return self.get_shares() * self.get_price()

    def get_ticker_line(self):
        return self.symbol + " | " + self.name  + " | " + str(self.shares)  + " | " + str(self.price) + " | " + str(self.get_value())

