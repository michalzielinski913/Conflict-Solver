from model.Comparator import Comparator
from model.StandardText import StandardText
from model.Splitter import Splitter
import tkinter as tk
from tkinter import filedialog
import eel

from model.StandardTextWriter import StandardTextWriter

"""
Most important class of the project, It controls flow of the program
"""
class Controller:

    def __init__(self):
        """
        Class constructor
        """
        pass

    def set_split_settings(self, mode, n):
        """
        Set settings for text splitting
        :param mode: splitting mode
        :param n: splitting size
        """
        self.mode = mode
        self.n = n

    def get_split_settings(self):
        """
        Getter for splitting settings
        :return:
        """
        return self.mode, self.n

    def third_file_path(self):
        """
        Open file dialog to choose location of third file
        """
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        file_path = filedialog.asksaveasfile(parent=root)
        return file_path.name

    def choose_file_path(self, wildcard="*"):
        """
        Open file dialog and choose text file
        :param wildcard: wildcard
        :return: String with path to the choosen text file
        """
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        file_path = filedialog.askopenfilename(parent=root)
        return file_path

    def solve_conflict(self, id_number, option, new_text=None):
        """
        Solve selected conflict
        :param id_number: Conflict ID
        :param option: How to solve conflict
        :param new_text: If custom text option was choosen this parameter contains its value
        :return:
        """
        eel.removeRow(id_number)
        eel.setLeftText("")
        eel.setRightText("")
        self.comparator.solve_conflict(int(id_number), option, new_text)

    def get_fragment(self, id_number):
        """
        Display two full text chunks in the UI based on ID
        :param id_number: conflict ID of given element
        :return:
        """
        text_one, text_two = self.comparator.get_element(int(id_number))
        eel.setLeftText(text_one)
        eel.setRightText(text_two)

    def cancel_compare(self):
        """
        Cancel text comparision
        :return:
        """
        self.cancel = True

    def split_files(self, data_one, data_two):
        """
        Split text files according to settings defined earlier
        :param data_one: Text one which will be splitted
        :param data_two: Text two which will be splitted
        :return: Two arrays, each contain splitted text
        """
        part_one = []
        part_two = []
        if self.mode == "line":
            part_one = self.splitter.chop_after_n_lines(data_one, self.n)
            part_two = self.splitter.chop_after_n_lines(data_two, self.n)
        elif self.mode == "char":
            part_one = self.splitter.chop_after_n_chars(data_one, self.n)
            part_two = self.splitter.chop_after_n_chars(data_two, self.n)
        elif self.mode == "word":
            part_one = self.splitter.chop_after_n_words(data_one, self.n)
            part_two = self.splitter.chop_after_n_words(data_two, self.n)
        elif self.mode == "sentence":
            part_one = self.splitter.chop_after_n_sentence(data_one, self.n)
            part_two = self.splitter.chop_after_n_sentence(data_two, self.n)
        return part_one, part_two

    def load_and_compare(self, path_one, path_two):
        """
        Load given text files and compare them
        :param path_one: Path to the first file
        :param path_two: Path to the second file
        """
        self.cancel = False
        self.splitter = Splitter()
        self.comparator=Comparator()
        x=0
        try:
            file_one = StandardText(path_one)
        except:
            eel.cancelCompare()
            eel.sendAlert("File: "+path_one+"\n Could not be opened!")
            return
        try:
            file_two = StandardText(path_two)
        except:
            eel.cancelCompare()
            eel.sendAlert("File: "+path_two+"\n Could not be opened!")
            return

        data_one = file_one.get_text()
        data_two = file_two.get_text()

        part_one, part_two = self.split_files(data_one, data_two)

        for element_one, element_two in zip(part_one, part_two):
            if self.cancel:
                return
            if x % 1000 == 0:
                eel.addRows(self.comparator.get_json())
                self.comparator.reset_json()
                eel.sleep(0.5)
            self.comparator.compare(element_one, element_two)
            x += 1

        eel.addRows(self.comparator.get_json())
        eel.sendAlert('Comparing complete!', '')
        self.comparator.reset_json()

    def generate_third_file(self, path):
        """
        Generate third file
        :param path: Path where third file will be stored
        """
        try:
            self.writer = StandardTextWriter(path)
        except:
            eel.sendAlert('File: ' + path + '\n Could not be created!')
            return
        for line in self.comparator.get_first_column():
            self.writer.write_line_to_file(line)
        self.writer.finish()
        eel.cancelCompare()
        eel.sendAlert('File: ' + path + '\n was generated!')
