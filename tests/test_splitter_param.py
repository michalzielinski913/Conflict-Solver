from parameterized import parameterized
from model.splitter import Splitter
import os
import unittest

data_path = (os.path.join(os.path.dirname(__file__), "TestFiles"))


def load_files(path, file_name):
    with open(os.path.join(path, file_name), 'r') as f:
        text = f.read().encode().decode('unicode_escape')
    return text


class TestSplitter(unittest.TestCase):
    @parameterized.expand([("FiftyCharsMultiLineInput.txt", "FiftyCharsMultiLineOutput.txt", 12),
                           ("FiftyCharsSingleLineInput.txt", "FiftyCharsSingleLineOutput.txt", 12),
                           ("TenCharsMultiLineInput.txt", "TenCharsMultiLineOutput.txt", 3),
                           ("TenCharsSingleLineInput.txt", "TenCharsSingleLineOutput.txt", 3),
                           ("LongArabicCharsInput.txt", "LongArabicCharsOutput.txt", 1)
                           ])
    def test_chop_after_n_chars(self, input, expected, split_value):
        splitter = Splitter
        temp_path = (os.path.join(data_path, "CharsSplitFiles"))
        input_text = load_files(temp_path, input)
        output_text = load_files(temp_path, expected)
        chop_output = splitter.chop_after_n_chars(input_text, split_value)
        output = ("\n".join(chop_output))
        self.assertEqual(output_text, output)

    @parameterized.expand([("FiftyWordsMultiLineInput.txt", "FiftyWordsMultiLineOutput.txt", 12),
                           ("FiftyWordsSingleLineInput.txt", "FiftyWordsSingleLineOutput.txt", 12),
                           ("LongWordsInput.txt", "LongWordsOutput.txt", 1),
                           ("TenWordsMultiLineInput.txt", "TenWordsMultiLineOutput.txt", 3),
                           ("TenWordsSingleLineInput.txt", "TenWordsSingleLineOutput.txt", 3)
                           ])
    def test_chop_after_n_words(self, input, expected, split_value):
        splitter = Splitter
        temp_path = (os.path.join(data_path, "WordsSplitFiles"))
        input_text = load_files(temp_path, input)
        output_text = load_files(temp_path, expected)
        chop_output = splitter.chop_after_n_words(input_text, split_value)
        output = ("\n".join(chop_output))
        self.assertEqual(output_text, output)

    @parameterized.expand([("FiftySentencesMultiLineInput.txt", "FiftySentencesMultiLineOutput.txt", 12),
                           ("FiftySentencesSingleLineInput.txt", "FiftySentencesSingleLineOutput.txt", 12),
                           ("LongSentencesInput.txt", "LongSentencesOutput.txt", 1),
                           ("TenSentencesMultiLineInput.txt", "TenSentencesMultiLineOutput.txt", 3),
                           ("TenSentencesSingleLineInput.txt", "TenSentencesSingleLineOutput.txt", 3)
                           ])
    def test_chop_after_n_sentence(self, input, expected, split_value):
        splitter = Splitter
        temp_path = (os.path.join(data_path, "SentencesSplitFiles"))
        input_text = load_files(temp_path, input)
        output_text = load_files(temp_path, expected)
        chop_output = splitter.chop_after_n_sentence(input_text, split_value)
        output = ("\n".join(chop_output))
        self.assertEqual(output_text, output)

    @parameterized.expand([("FiftyLinesFiveInput.txt", "FiftyLinesFiveOutput.txt", 5),
                           ("FiftyLinesTwelveInput.txt", "FiftyLinesTwelveOutput.txt", 12),
                           ("LongLinesInput.txt", "LongLinesOutput.txt", 1),
                           ("TenLinesOneInput.txt", "TenLinesOneOutput.txt", 1),
                           ("TenLinesThreeInput.txt", "TenLinesThreeOutput.txt", 3)
                           ])
    def test_chop_after_n_lines(self, input, expected, split_value):
        splitter = Splitter
        temp_path = (os.path.join(data_path, "LinesSplitFiles"))
        input_text = load_files(temp_path, input)
        output_text = load_files(temp_path, expected)
        chop_output = splitter.chop_after_n_lines(input_text, split_value)
        output = ("".join(chop_output))
        self.assertEqual(output_text, output)
