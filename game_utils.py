''' things that are helpful '''

from stock import Stock
class GameUtils(object):
    @staticmethod
    def main_menu():
        menu_string = ''' What would you like to do?
        (C)ontinue
        (Q)uit'''
        return raw_input(menu_string)
