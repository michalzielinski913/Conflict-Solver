from parameterized import parameterized_class
from model.StandardTextWriter import StandardTextWriter

import os
import filecmp
import unittest

data_path = (os.path.join(os.path.dirname(__file__), "mergeTestFiles"))

class TestMathUnitTest(unittest.TestCase):

    @parameterized_class(('input', 'expected'), [
        ("FileInput1.txt", "FileOutput1.txt"),
        ("FileInput2.txt", "FileOutput2.txt"),
        ("FileInput3.txt", "FileOutput3.txt"),
        ("FileInput4.txt", "FileOutput4.txt"),
        ("FileInput5.txt", "FileOutput5.txt"),
        ("FileInput6.txt", "FileOutput6.txt"),
        ("FileInput7.txt", "FileOutput7.txt"),
        ("FileInput8.txt", "FileOutput8.txt")
    ])
    class TestMathClass(unittest.TestCase):
        def test_merge(self, input, expected):
            with open(data_path + "/input/" + input, 'r') as input_file:
                input_text = input_file.readlines()
            merged_text = merge_text(input_text)
            output = open(data_path + "/output/" + expected, 'r')
            self.assertTrue(merged_text==