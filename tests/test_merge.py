from parameterized import parameterized_class
from model.StandardTextWriter import StandardTextWriter

import os
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
            text_writer = StandardTextWriter(data_path + "/result.txt")
            for text in input_text:
                text_writer.writeLineToFile(text)
            expected = open(data_path + "/output/" + self.expected, 'r').read().encode().decode('unicode_escape')
            result = open(data_path + "/result.txt", "r").read().encode().decode('unicode_escape')
            self.assertEqual(expected, result)