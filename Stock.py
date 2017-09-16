class Stock:

    def __init__(self, symbol, name, shares=0, price=0):
        self.symbol = symbol
        self.shares = shares
        self.price = price
        self.name = name


    def getName(self):
        return self.name
        
    def setName(self, newname):
        self.name = newname

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, newSymbol):
        self.symbol = newSymbol

    def getPrice(self):
        return self.price

    def setPrice(self, newamt):
        self.price = newamt

    def getShares(self):
        return self.shares

    def setShares(self, newamt):
        self.shares = newamt

    def addShares(self, addition):
        self.shares += addition

    def subShares(self, deduction):
        self.shares -= deduction

    def getTickerLine(self):
        return self.symbol + " | " + self.name  + " | " + str(self.shares)  + " | " + str(self.price)


