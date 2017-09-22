''' test the code '''
from stock import Stock
from global_market import GlobalMarket


def main():

    TESTER1 = Stock("MMM", "Moneymust", 100, 100)
    TESTER2 = Stock("ABC", "Alphabet", 182, 1132)
    TESTER3 = Stock("IBM", "International Business Machines", 113, 1789)

    print 
    #tick = raw_input("Enter the symbol of the stock (3 letters)")
    #name = raw_input("Enter the name of the stock ")

    #TESTER4 = Stock(tick, name, 756, 188)

    gm = GlobalMarket()
    gm.add_stock(TESTER1)
    gm.add_stock(TESTER2)
    gm.add_stock(TESTER3)
    #gm.add_stock(TESTER4)

    for stock in gm.get_global_market_stocks():
        print stock.get_ticker_line()

    print str(gm.get_global_market_value())

    stopped = False
    gm.prepare()
    while not stopped:
        stopped = gm.process()
        gm.update()



if __name__ == '__main__':
    main()
    