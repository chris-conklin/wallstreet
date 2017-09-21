''' things that are helpful '''

from stock import Stock
class GameUtils(object):
    @staticmethod
    def main_menu():
        menu_string = '''What would you like to do?\n(C)ontinue\n(Q)uit\n? '''
        return raw_input(menu_string).upper()

    @staticmethod
    def get_game_type():
        menu_string = "Is this a (N)ew or (E)xisting game\n?"
        return raw_input(menu_string).upper()
    
        