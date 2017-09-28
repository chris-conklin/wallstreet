class Investment(object):
    def __init__(self):
        self.high = 0
        self.low = 0
        self.type = 'super'

    def get_value(self):
        raise NotImplementedError

    def get_ticker_line(self):
        pass