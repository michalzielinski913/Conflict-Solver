from parameterized import parameterized_class
# HERE IMPORT METHOD TO MERGE 3RD FILE

import os
import filecmp
import unittest

data_path = (os.path.join(os.path.dirname(__file__), "mergeTestFiles"))

class TestMergeUnitTest(unittest.TestCase):

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
    class TestMergeClass(unittest.TestCase):
        def test_merge(self):
            with open(data_path + "/input/" + self.input, 'r') as input_file:
                input_text = input_file.read().splitlines()
            merged_text = merge_text(input_text) # CHANGE METHOD NAME TO CORRECT ONE
            output = open(data_path + "/output/" + self.expected, 'r')
            self.assertEqual(merged_text, output.read())