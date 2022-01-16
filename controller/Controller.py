from model.Comparator import Comparator
from model.StandardText import StandardText
from model.Splitter import Splitter
import tkinter as tk
from tkinter import filedialog
import eel

from model.StandardTextWriter import StandardTextWriter


class Controller:

    def __init__(self):
        self.splitter = Splitter()
        self.comparator = Comparator()
        self.mode = ''
        self.n = ''
        self.cancel = False
        self.writer = None

    def set_split_settings(self, mode, n):
        self.mode = mode
        self.n = n

    def get_split_settings(self):
        return self.mode, self.n

    def choose_file_path(self, wildcard="*"):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def solve_conflict(self, id_number, option, new_text=None):
        eel.removeRow(id_number)
        eel.setLeftText("")
        eel.setRightText("")
        pass

    def get_fragment(self, id_number):
        text_one, text_two = self.comparator.get_element(int(id_number))
        eel.setLeftText(text_one)
        eel.setRightText(text_two)

    def cancel_compare(self):
        self.cancel = True
        pass

    def split_files(self, data_one, data_two):
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
        self.cancel = False

        x = 0

        try:
            file_one = StandardText(path_one)
        except:
            eel.emergencyCancel()
            eel.sendAlert("File: " + path_one + "\n Could not be opened!")
            return
        try:
            file_two = StandardText(path_two)
        except:
            eel.emergencyCancel()
            eel.sendAlert("File: " + path_two + "\n Could not be opened!")
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
        try:
            self.writer = StandardTextWriter(path)
        except:
            eel.sendAlert('File: ' + path + '\n Could not be created!')
            return
        for line in self.comparator.get_first_column():
            self.writer.write_line_to_file(line)
        eel.cancelCompare()
        eel.sendAlert('File: ' + path + '\n was generated!')
