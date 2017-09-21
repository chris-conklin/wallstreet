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
        self.rountcnt = 0

    def prepare(self):
        # is this a new or existing game?
        choice = raw_input("Is this a (N)ew or (E)xisting game?")
        if ''.upper(choice) == 'N':
            self.new_game()
        else:
            self.load_game()
    
    def new_game(self):
        print "We're getting kinda rabbit holed!"

    def load_game(self):
        print "We're not there yet"

    def get_global_market_value(self):
        '''return the total net worth of stocks,funds and comm'''
        total = 0
        # TODO: Could this be a superclass with subclass
        # objects that each have a get_value method??
        for S in self.stocks:
            total += (S.get_shares() * S.get_price())
        for F in self.funds:
            total += F.get_value()
        for C in self.commodities:
            total += C.get_value()
        return total

    def get_global_market_stocks(self):
        ''' return a list of stocks '''
        return self.stocks

    def add_stock(self, new_stock):
        ''' Add a Stock to the GM '''
        self.stocks.append(new_stock)

    def process(self):
        return False

    def update(self):
        ''' update all global_market stuff to simulate activity '''
        # stocks

        # funds

        # commodities



