from stock import Stock
import game_utils as gutils

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
        choice = gutils.get_game_type()
        if choice.upper() == 'N':
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
        for stk in self.stocks:
            total += stk.get_value()
        for fnd in self.funds:
            total += fnd.get_value()
        for cty in self.commodities:
            total += cty.get_value()
        return total

    def get_global_market_stocks(self):
        ''' return a list of stocks '''
        return self.stocks

    def add_stock(self, new_stock):
        ''' Add a Stock to the GM '''
        self.stocks.append(new_stock)

    def process(self):
        choice = gutils.main_menu()
        if choice == 'C':
            return False
        else:
            return True

    def update(self):
        ''' update all global_market stuff to simulate activity '''
        self.rountcnt += 1
        # stocks

        # funds

        # commodities



