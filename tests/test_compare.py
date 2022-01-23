import re

from parameterized import parameterized_class
from model.Comparator import Comparator
import os
import unittest

data_path = (os.path.join(os.path.dirname(__file__), "compareTestFiles"))

"""Test class responsible for testing compare function of program"""
@parameterized_class(('first_file', 'second_file', 'expected'), [
    ("File1.txt", "File1.txt", [1, 9, 16, 21, 22]),
    ("File2.txt", "File2.txt", [4, 7, 16, 35, 44]),
    ("File3.txt", "File3.txt", [4, 23, 36, 42, 58, 61]),
    ("File4.txt", "File4.txt", [1, 14, 35, 44]),
    ("File5.txt", "File5.txt", [2, 7, 15, 26]),
    ("File6.txt", "File6.txt", [15, 16, 27, 35, 58]),
    ("File7.txt", "File7.txt", [1, 4, 5]),
    ("File8.txt", "File8.txt", [3, 12, 19, 20])
])
class TestCompareClass(unittest.TestCase):
    def test_compare(self):
        comp=Comparator()
        with open(data_path + "/firstFile/" + self.first_file, 'r') as first_file:
            first_text = first_file.readlines()
        with open(data_path + "/secondFile/" + self.second_file, 'r') as second_file:
            second_text = second_file.readlines()
        maks = max(len(first_text),len(second_text))
        if len(first_text) < len(second_text):
            for i in range(0, maks):
                if i < len(first_text):
                    comp.compare(first_text[i], second_text[i])
                else:
                    comp.compare("",second_text[i])
        else:
            for i in range(0, maks):
                if i < len(second_text):
                    comp.compare(first_text[i], second_text[i])
                else:
                    comp.compare(first_text[i], "")
        json_file=comp.getJson()
        pattern = '"DT_RowId": ([0-9]*?),'
        list = re.findall(pattern, json_file)
        for i in range(0,len(list)):
            list[i] = int(list[i])
        comp.resetJson()
        self.assertEqual(self.expected, list)