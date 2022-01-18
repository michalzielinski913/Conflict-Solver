import unittest
import os
import time
from model.splitter import Splitter


data_path = (os.path.join(os.path.dirname(__file__), "TestFiles"))
input_filename_list = []
output_filename_list = []


def load_files_input(num):
    input_list = []
    if num == 1:
        temp_path = (os.path.join(data_path, "CharsSplitFiles"))

    elif num == 2:
        temp_path = (os.path.join(data_path, "WordsSplitFiles"))

    elif num == 3:
        temp_path = (os.path.join(data_path, "SentencesSplitFiles"))

    else:
        temp_path = (os.path.join(data_path, "LinesSplitFiles"))

    for root, dirs, files in os.walk(temp_path):
        for file in files:
            if file.endswith('Input.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    text = f.read()
                    input_list.append(text)
                    input_filename_list.append(file)
    return input_list


def load_files_output(num):
    output_list = []
    if num == 1:
        temp_path = (os.path.join(data_path, "CharsSplitFiles"))

    elif num == 2:
        temp_path = (os.path.join(data_path, "WordsSplitFiles"))

    elif num == 3:
        temp_path = (os.path.join(data_path, "SentencesSplitFiles"))

    else:
        temp_path = (os.path.join(data_path, "LinesSplitFiles"))

    for root, dirs, files in os.walk(temp_path):
        for file in files:
            if file.endswith('Output.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    text = f.read().encode().decode('unicode_escape')
                    output_list.append(text)
                    output_filename_list.append(file)
    return output_list


class TestSplitter(unittest.TestCase):

    def test_chop_after_n_chars(self):
        start = time.perf_counter()
        splitter = Splitter
        num = 1
        input_list = load_files_input(num)
        output_list = load_files_output(num)
        for i in range(len(input_list)):
            if "Fifty" in input_filename_list[i]:
                test_result = splitter.chop_after_n_chars(input_list[i], 12)
            elif "Ten" in input_filename_list[i]:
                test_result = splitter.chop_after_n_chars(input_list[i], 3)
            elif "Long" in input_filename_list[i]:
                test_result = splitter.chop_after_n_chars(input_list[i], 1)
            else:
                pass
            output = ("\n".join(test_result))
            self.assertEqual(output_list[i], output, "Test failed with files " + input_filename_list[i] + " and "
                             + output_filename_list[i] + ".")
        stop = time.perf_counter()
        print(f" test_chop_after_n_chars elapsed is {start - stop:0.4f} seconds. Tested with "
              + "{}".format(len(input_list)) + " files.")
        print(input_filename_list)
        print(output_filename_list)
        input_filename_list.clear()
        output_filename_list.clear()

    def test_chop_after_n_words(self):
        start = time.perf_counter()
        splitter = Splitter
        num = 2
        input_list = load_files_input(num)
        output_list = load_files_output(num)
        for i in range(len(input_list)):
            if "Fifty" in input_filename_list[i]:
                test_result = splitter.chop_after_n_words(input_list[i], 12)
            elif "Ten" in input_filename_list[i]:
                test_result = splitter.chop_after_n_words(input_list[i], 3)
            elif "Long" in input_filename_list[i]:
                test_result = splitter.chop_after_n_words(input_list[i], 1)
            else:
                pass
            output = ("\n".join(test_result))
            self.assertEqual(output_list[i], output, "Test failed with files " + input_filename_list[i] + " and "
                             + output_filename_list[i] + ".")

        stop = time.perf_counter()
        print(f" test_chop_after_n_words elapsed is {start - stop:0.4f} seconds. Tested with "
              + "{}".format(len(input_list)) + " files.")
        print(input_filename_list)
        print(output_filename_list)
        input_filename_list.clear()
        output_filename_list.clear()

    def test_chop_after_n_sentence(self):
        start = time.perf_counter()
        splitter = Splitter
        num = 3
        input_list = load_files_input(num)
        output_list = load_files_output(num)
        for i in range(len(input_list)):
            if "Fifty" in input_filename_list[i]:
                test_result = splitter.chop_after_n_sentence(input_list[i], 12)
            elif "Ten" in input_filename_list[i]:
                test_result = splitter.chop_after_n_sentence(input_list[i], 3)
            elif "Long" in input_filename_list[i]:
                test_result = splitter.chop_after_n_sentence(input_list[i], 1)
            else:
                pass
            output = ("\n".join(test_result))
            self.assertEqual(output_list[i], output, "Test failed with files " + input_filename_list[i] + " and "
                             + output_filename_list[i] + ".")

        stop = time.perf_counter()
        print(f" test_chop_after_n_sentence elapsed is {start - stop:0.4f} seconds. Tested with "
              + "{}".format(len(input_list)) + " files.")
        print(input_filename_list)
        print(output_filename_list)
        input_filename_list.clear()
        output_filename_list.clear()

    def test_chop_after_n_lines(self):
        start = time.perf_counter()
        splitter = Splitter
        temp_arr = [5, 12, 1, 3]
        num = 4
        input_list = load_files_input(num)
        output_list = load_files_output(num)
        for i in range(len(input_list)):
            if "One" or "Long" in input_filename_list[i]:
                test_result = splitter.chop_after_n_lines(input_list[i], 1)
            elif "Three" in input_filename_list[i]:
                test_result = splitter.chop_after_n_lines(input_list[i], 3)
            elif "Five" in input_filename_list[i]:
                test_result = splitter.chop_after_n_lines(input_list[i], 5)
            elif "Twelve" in input_filename_list[i]:
                test_result = splitter.chop_after_n_lines(input_list[i], 12)
            else:
                pass
            output = ("".join(test_result))
            self.assertEqual(output_list[i], output, "Test failed with files " + input_filename_list[i] + " and "
                             + output_filename_list[i] + ".")

        stop = time.perf_counter()
        print(f" test_chop_after_n_lines elapsed is {start - stop:0.4f} seconds. Tested with "
              + "{}".format(len(input_list)) + " files.")
        print(input_filename_list)
        print(output_filename_list)
        input_filename_list.clear()
        output_filename_list.clear()
