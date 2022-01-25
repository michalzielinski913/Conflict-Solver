import eel
from controller.Controller import Controller
"""
Main project file, It must be executed in order to run program
It contains set of 'friend' functions which can be utilized by javascript layer of application
"""

eel.init('web')
controller=Controller()


@eel.expose
def get_file_path(wildcard='*'):
    """
    Open file dialog where user can select text file
    :param wildcard: wildcard import
    :return: String containing path to the choosen file
    """
    return controller.choose_file_path()


@eel.expose
def load_and_compare(path_one, path_two):
    """
    Compare two text files
    :param path_one: Path to file one
    :param path_two: Path to file two
    """
    controller.load_and_compare(path_one, path_two)

@eel.expose
def get_fragment(id_number):
    """
    Display full text chunk for difference with given id
    :param id_number: ID of chunk which user want to display
    """
    controller.get_fragment(id_number)


@eel.expose
def solve_conflict(id_number, option, new_text=None):
    """
    Solve conflict between two text chunks
    :param id_number: ID number of difference
    :param option: Which option is used for solving
    :param new_text: If custom option was choosen it represents new value
    """
    controller.solve_conflict(id_number, option, new_text)


@eel.expose
def set_split_settings(mode, N):
    """
    Set settings how text file will be split
    :param mode: Which mode is used for splitting
    :param N: size of chunk
    """
    controller.set_split_settings(mode, N)


@eel.expose
def cancel_compare():
    """
    Cancel comparing
    """
    controller.cancel_compare()

@eel.expose
def generate_third_file(path):
    """
    Generate third file saved in given location
    :param path: Location of third file
    """
    controller.generate_third_file(path)

@eel.expose
def third_file_path():
    """
    Set location of third (merged) file
    """
    return controller.third_file_path()

eel.start('main.html')
