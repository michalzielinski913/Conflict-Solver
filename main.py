import eel
from controller.Controller import Controler
###TODO###
#Input validation
#Notifications about errors/finish in UI
#3rd file generation
#Solve file browser problems (window opens in the background)
# TESTS

eel.init('web')

controller=Controler()


@eel.expose
def get_file_path(wildcard='*'):
    return controller.choose_file_path()


@eel.expose
def load_and_compare(path_one, path_two):
    controller.load_and_compare(path_one, path_two)

#C:/Users/Michał/Downloads/długieLoremIpsum2.txt


@eel.expose
def get_fragment(id_number):
    controller.get_fragment(id_number)


@eel.expose
def solve_conflict(id_number, option, new_text=None):
    controller.solve_conflict(id_number, option, new_text)


@eel.expose
def set_split_settings(mode, N):
    controller.set_split_settings(mode, N)


@eel.expose
def cancel_compare():
    controller.cancel_compare()


eel.start('main.html')
