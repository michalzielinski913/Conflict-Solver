import re

from parameterized import parameterized_class
from model.Comparator import Comparator
import os
import unittest

data_path = (os.path.join(os.path.dirname(__file__), "compareTestFiles"))

"""Test class responsible for testing compare function of program"""
@parameterized_class(('first_file', 'second_file', 'expected_json'), [
    ("File1.txt", "File1.txt", "json1.txt"),
    ("File2.txt", "File2.txt", "json2.txt"),
    ("File3.txt", "File3.txt", "json3.txt"),
    ("File4.txt", "File4.txt", "json4.txt"),
    ("File5.txt", "File5.txt", "json5.txt"),
    ("File6.txt", "File6.txt", "json6.txt"),
    ("File7.txt", "File7.txt", "json7.txt"),
    ("File8.txt", "File8.txt", "json8.txt")
])
class TestCompareClass(unittest.TestCase):
    def test_compare(self):
        comp=Comparator()
        with open(data_path + "/firstFile/" + self.first_file, 'r') as first_file:
            first_text = first_file.readlines()
        with open(data_path + "/secondFile/" + self.second_file, 'r') as second_file:
            second_text = second_file.readlines()
        with open(data_path + "/json/" + self.expected_json, 'r') as json_file:
            expected = json_file.read()
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
        json = comp.getJson()
        comp.resetJson()
        self.assertEqual(expected, json)