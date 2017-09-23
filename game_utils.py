''' things that are helpful '''

from stock import Stock

def main_menu():
    valid_inputs = ['C', 'c', 'Q','q']
    menu_string = '''What would you like to do?\n(C)ontinue\n(Q)uit\n? '''
    k = raw_input(menu_string).upper()
    while k not in valid_inputs:
        print
        print ">>> Invalid Selection!"
        print
        k = raw_input(menu_string).upper()
    return k

def get_game_type():
    menu_string = '''Is this a (N)ew or (E)xisting game\n? '''
    return raw_input(menu_string).upper()

# maybe this should be a global_market object return?
''' load game settings from file '''
def load_saved_game(gamefile):
    ''' read game stuff '''
    with open(gamefile, 'r') as oldgame:
        pass
