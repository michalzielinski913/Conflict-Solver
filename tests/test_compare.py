from parameterized import parameterized_class
# HERE IMPORT METHOD TO COMPARE 

import os
import unittest

data_path = (os.path.join(os.path.dirname(__file__), "compareTestFiles"))

class TestCompareUnitTest(unittest.TestCase):

    @parameterized_class(('first_file', 'second_file', 'expected'), [
        ("File1.txt", "File1.txt", [0,8,16])
        ("File2.txt", "File2.txt", [3,6,43]),
        ("File3.txt", "File3.txt", [3,22,57,60]),
        ("File4.txt", "File4.txt", [0,13,34,43]),
        ("File5.txt", "File5.txt", [1,6,14,25]),
        ("File6.txt", "File6.txt", [14,15,26,57]),
        ("File7.txt", "File7.txt", [0,3,4]),
        ("File8.txt", "File8.txt", [4,18,19])
    ])
    class TestCompareClass(unittest.TestCase):
        def test_compare(self):
            with open(data_path + "/firstFile/" + self.first_file, 'r') as first_file:
                first_text = first_file.readlines()
            with open(data_path + "/secondFile/" + self.second_file, 'r') as second_file:
                second_text = second_file.readlines()
            difference_list = compare(first_text, second_text)  # CHANGE METHOD NAME TO CORRECT ONE / METHOD SHOULD RETURN LIST WITH INDEXES WHERE DIFFERENCE OCCURES
            self.assertEqual(difference_list, self.expected)