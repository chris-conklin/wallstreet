
from stock import Stock
import game_utils as gutils


def generate_stock(id, name):
    initial_shares = gutils.get_random_integer(100,10000)
    share_price = gutils.get_random_float(.5, 250.0)
    return Stock(id, name, intial_shares, share_price)



