import fund
import game_utils as gutils

def generate_fund(title, valmin = 0, valmax = 1000, pctmin = .001, pctmax = .05):
    
    startval = gutils.get_random_integer(valmin, valmax)
    startpct = gutils.get_random_float(pctmin, pctmax)
    return fund.Fund(title, startval, startpct)