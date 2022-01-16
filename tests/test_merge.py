import filecmp

from nose.tools import assert_equal
from nose.tools import assert_true
from parameterized import parameterized, parameterized_class

import os
import unittest

data_path = (os.path.join(os.path.dirname(__file__), "MergeTestFiles"))

class TestMathUnitTest(unittest.TestCase):

    @parameterized_class(('input', 'expected'), [
        ("FileOneInput.txt", "FileOneOutput.txt"),
        ("FileTwoInput.txt", "FileTwoOutput.txt"),
        ("FileThreeInput.txt", "FileThreeOutput.txt"),
        ("FileFourInput.txt", "FileFourOutput")
    ])
    class TestMathClass(unittest.TestCase):
        def  merge_text(self, flag, input):
            with open(os.path.join(data_path, input), 'r') as input_file:
                input_text = input_file.read()
            if flag == 1:
                merged_file = merge_chars(input_text)
            elif flag == 2:
                merged_file = merge_words(input_text)
            elif flag == 3:
                merged_file = merge_sentences(input_text)
            elif flag == 4:
                merged_file = merge_lines(input_text)
            return merged_file

        def test_merge_chars(self, input, expected):
            merged_file = merge_text(1, input)
            self.assertTrue(filecmp.cmp(merged_file, expected, shallow=False))

        def test_merge_words(self, input, expected):
            merged_file = merge_text(2, input)
            self.assertTrue(filecmp.cmp(merged_file, expected, shallow=False))

        def test_merge_sentences(self, input, expected):
            merged_file = merge_text(3, input)
            self.assertTrue(filecmp.cmp(merged_file, expected, shallow=False))

        def test_merge_lines(self, input, expected):
            merged_file = merge_text(4, input)
            self.assertTrue(filecmp.cmp(merged_file, expected, shallow=False))

        #     If symbol merging implemented
        # def test_merge(self, input, expected):
        #     with open(os.path.join(data_path, input), 'r') as input_file:
        #         input_text = input_file.read()
        #     merged_file = merge_text(input_text)
        #     self.assertTrue(filecmp.cmp(merged_file, expected, shallow=False))