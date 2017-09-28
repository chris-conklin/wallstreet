''' test the code '''

from global_market import GlobalMarket
import stock_manager


def main():

    TESTER1 = stock_manager.generate_stock("MMM", "Moneymust", 1, 75, 250, 1200)
    TESTER2 = stock_manager.generate_stock("ABC", "Alphabet", 12, 75, 250, 1100)
    TESTER3 = stock_manager.generate_stock("IBM", "International Business Machines")

    TESTER4 = stock_manager.generate_stock("MCI","Metro Communications Inc")

    print 
    #tick = raw_input("Enter the symbol of the stock (3 letters)")
    #name = raw_input("Enter the name of the stock ")

    #TESTER4 = Stock(tick, name, 756, 188)

    gm = GlobalMarket()
    stopped = False
    gm.prepare()
    while not stopped:
        stopped = gm.process()
        gm.update()

    for stock in gm.get_global_market_stocks():
        print stock.get_ticker_line()

    print str(gm.get_global_market_value())


if __name__ == '__main__':
    main()
    