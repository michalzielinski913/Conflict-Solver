import eel
from controller.Controller import Controller
###TODO###
#Input validation
#Notifications about errors/finish in UI Edit: added simple version
#3rd file generation, EDIT: added 3rd file generation but some fixes are needed
#Solve file browser problems (window opens in the background)
# TESTS

eel.init('web')

controller=Controller()


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

@eel.expose
def generate_third_file(path):
    controller.generate_third_file(path)


eel.start('main.html')
