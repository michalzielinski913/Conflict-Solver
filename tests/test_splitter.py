import unittest
import os
from model.splitter import Splitter

data_path = (os.path.join(os.path.dirname(__file__), "TestFiles"))


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
    return output_list


class TestSplitter(unittest.TestCase):

    def test_chop_after_n_chars(self):
        splitter = Splitter
        num = 1
        input_list = load_files_input(num)
        output_list = load_files_output(num)
        for i in range(0, 3):
            if i < 2:
                test_result = splitter.chop_after_n_chars(input_list[i], 12)
            else:
                test_result = splitter.chop_after_n_chars(input_list[i], 3)
            output = ("\n".join(test_result))
            self.assertEqual(output_list[i], output)

    def test_chop_after_n_words(self):
        splitter = Splitter
        num = 2
        input_list = load_files_input(num)
        output_list = load_files_output(num)
        for i in range(0, 3):
            if i < 2:
                test_result = splitter.chop_after_n_words(input_list[i], 12)
            else:
                test_result = splitter.chop_after_n_words(input_list[i], 3)
            output = ("\n".join(test_result))
            self.assertEqual(output_list[i], output)

    def test_chop_after_n_sentence(self):
        splitter = Splitter
        num = 3
        input_list = load_files_input(num)
        output_list = load_files_output(num)
        for i in range(0, 3):
            if i < 2:
                test_result = splitter.chop_after_n_sentence(input_list[i], 12)
            else:
                test_result = splitter.chop_after_n_sentence(input_list[i], 3)
            output = ("\n".join(test_result))
            self.assertEqual(output_list[i], output)

    def test_chop_after_n_lines(self):
        splitter = Splitter
        temp_arr = [5, 12, 1, 3]
        num = 4
        input_list = load_files_input(num)
        output_list = load_files_output(num)
        for i in range(0, 3):
            test_result = splitter.chop_after_n_lines(input_list[i], temp_arr[i])
            output = ("\n".join(test_result))
            self.assertEqual(output_list[i], output)
