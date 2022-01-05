import unittest
from model.Splitter import Splitter


class TestSplitter(unittest.TestCase):

    def test_chopAfterNChars(self):
        self.splitter = Splitter()
        data = "Jane is tall."
        result = self.splitter.chopAfterNChars(data, 5)
        print(result)
        self.assertEqual(result, ["Jane ", "is ta", "ll."])

    def test_chopAfterNWords(self):
        self.splitter = Splitter()
        data = "Jane is tall."
        result = self.splitter.chopAfterNWords(data, 1)
        print(result)
        self.assertEqual(result, ["Jane", "is", "tall."])

    def test_chopAfterNSentence(self):
        self.splitter = Splitter()
        data = "Jane is tall. Cody is short"
        result = self.splitter.chopAfterNSentence(data, 1)
        print(result)
        self.assertEqual(result, ["Jane is tall.", "Cody is short"])

    def test_chopAfterNLines(self):
        self.splitter = Splitter()
        data = """Jane is tall.
Cody is short."""
        result = self.splitter.chopAfterNLines(data, 1)
        print(result)
        self.assertEqual(result, ["Jane is tall.\n", "Cody is short."])