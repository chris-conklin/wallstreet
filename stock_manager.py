
from stock import Stock
import game_utils as gutils


def generate_stock(id, name, min_price = 0, max_price = 250, min_shares = 100 , max_shares = 10000):
    initial_shares = gutils.get_random_integer(min_shares, max_shares)
    share_price = gutils.get_random_float(float(min_price), float(max_price))
    return Stock(id, name, initial_shares, share_price)



