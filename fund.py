from investment import Investment

''' The fund class '''
class Fund(Investment):
    ''' The fund class '''
    def __init__(self, title):
        self.title = title
        self.value = 0
        self.current_rate = 0
        self.rate_high = 0
        self.rate_low = 0
    
    def set_title(self, newtitle):
        self.title = newtitle

    def get_title(self):
        return self.title

    def set_current_rate(self, newrate):
        self.current_rate = newrate

    def get_current_rate(self):
        return self.current_rate

    def set_rate_high(self, high):
        self.rate_high = high
    
    def get_rate_high(self):
        return self.rate_high

    def set_rate_low(self, newlow):
        self.rate_low = newlow

    def set_value(self, newvalue):
        self.value = newvalue

    def get_value(self):
        return self.value

    def get_ticker_line(self):
        return self.title + " | " + str(self.value)  + " | " + str(self.current_rate)