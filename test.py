''' test the code '''

from global_market import GlobalMarket
import stock_manager


def main():


    gm = GlobalMarket()
    stopped = False
    gm.prepare()
    while not stopped:
        stopped = gm.process()
        gm.update()

    for stock in gm.get_global_market_stocks():
        print stock.get_ticker_line()

    for fund in gm.get_global_market_funds():
        print fund.get_ticker_line()
        
    print str(gm.get_global_market_value())


if __name__ == '__main__':
    main()
    