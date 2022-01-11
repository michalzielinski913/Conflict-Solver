import unittest
import os
from model.splitter import Splitter

data_path = os.path.dirname(__file__)


class TestSplitter(unittest.TestCase):

    def test_chopAfterNChars(self):
        splitter = Splitter
        file1 = open(os.path.join(data_path, "TenCharsSingleLineInput.txt"), "r")
        file2 = open(os.path.join(data_path, "TenCharsMultiLineInput.txt"), "r")
        file3 = open(os.path.join(data_path, "FiftyCharsSingleLineInput.txt"), "r")
        file4 = open(os.path.join(data_path, "FiftyCharsMultiLineInput.txt"), "r")

        file1_res = open(os.path.join(data_path, "TenCharsSingleLineOutput.txt"), "r")
        file2_res = open(os.path.join(data_path, "TenCharsMultiLineOutput.txt"), "r")
        file3_res = open(os.path.join(data_path, "FiftyCharsSingleLineOutput.txt"), "r")
        file4_res = open(os.path.join(data_path, "FiftyCharsMultiLineOutput.txt"), "r")

        data1 = file1.read()
        data2 = file2.read()
        data3 = file3.read()
        data4 = file4.read()

        result1 = file1_res.read()
        result2 = file2_res.read()
        result3 = file3_res.read()
        result4 = file4_res.read()

        test_result1 = splitter.chopAfterNChars(data1, 3)
        test_result2 = splitter.chopAfterNChars(data2, 3)
        test_result3 = splitter.chopAfterNChars(data3, 12)
        test_result4 = splitter.chopAfterNChars(data4, 12)

        output1 = ("\n".join(test_result1))
        output2 = ("\n".join(test_result2))
        output3 = ("\n".join(test_result3))
        output4 = ("\n".join(test_result4))

        self.assertEqual(result1, output1)
        self.assertEqual(result2, output2)
        self.assertEqual(result3, output3)
        self.assertEqual(result4, output4)

        file1.close()
        file2.close()
        file3.close()
        file4.close()

        file1_res.close()
        file2_res.close()
        file3_res.close()
        file4_res.close()

    def test_chopAfterNWords(self):
        splitter = Splitter
        file1 = open(os.path.join(data_path, "TenWordsSingleLineInput.txt"), "r")
        file2 = open(os.path.join(data_path, "TenWordsMultiLineInput.txt"), "r")
        file3 = open(os.path.join(data_path, "FiftyWordsSingleLineInput.txt"), "r")
        file4 = open(os.path.join(data_path, "FiftyWordsMultiLineInput.txt"), "r")

        file1_res = open(os.path.join(data_path, "TenWordsSingleLineOutput.txt"), "r")
        file2_res = open(os.path.join(data_path, "TenWordsMultiLineOutput.txt"), "r")
        file3_res = open(os.path.join(data_path, "FiftyWordsSingleLineOutput.txt"), "r")
        file4_res = open(os.path.join(data_path, "FiftyWordsMultiLineOutput.txt"), "r")

        data1 = file1.read()
        data2 = file2.read()
        data3 = file3.read()
        data4 = file4.read()

        result1 = file1_res.read()
        result2 = file2_res.read()
        result3 = file3_res.read()
        result4 = file4_res.read()

        test_result1 = splitter.chopAfterNWords(data1, 3)
        test_result2 = splitter.chopAfterNWords(data2, 3)
        test_result3 = splitter.chopAfterNWords(data3, 12)
        test_result4 = splitter.chopAfterNWords(data4, 12)

        output1 = ("\n".join(test_result1))
        output2 = ("\n".join(test_result2))
        output3 = ("\n".join(test_result3))
        output4 = ("\n".join(test_result4))

        self.assertEqual(result1, output1)
        self.assertEqual(result2, output2)
        self.assertEqual(result3, output3)
        self.assertEqual(result4, output4)

        file1.close()
        file2.close()
        file3.close()
        file4.close()

        file1_res.close()
        file2_res.close()
        file3_res.close()
        file4_res.close()

    def test_chopAfterNSentence(self):
        splitter = Splitter
        file1 = open(os.path.join(data_path, "TenSentencesSingleLineInput.txt"), "r")
        file2 = open(os.path.join(data_path, "TenSentencesMultiLineInput.txt"), "r")
        file3 = open(os.path.join(data_path, "FiftySentencesSingleLineInput.txt"), "r")
        file4 = open(os.path.join(data_path, "FiftySentencesMultiLineInput.txt"), "r")

        file1_res = open(os.path.join(data_path, "TenSentencesSingleLineOutput.txt"), "r")
        file2_res = open(os.path.join(data_path, "TenSentencesMultiLineOutput.txt"), "r")
        file3_res = open(os.path.join(data_path, "FiftySentencesSingleLineOutput.txt"), "r")
        file4_res = open(os.path.join(data_path, "FiftySentencesMultiLineOutput.txt"), "r")

        data1 = file1.read()
        data2 = file2.read()
        data3 = file3.read()
        data4 = file4.read()

        result1 = file1_res.read()
        result2 = file2_res.read()
        result3 = file3_res.read()
        result4 = file4_res.read()

        test_result1 = splitter.chopAfterNSentence(data1, 3)
        test_result2 = splitter.chopAfterNSentence(data2, 3)
        test_result3 = splitter.chopAfterNSentence(data3, 12)
        test_result4 = splitter.chopAfterNSentence(data4, 12)

        output1 = ("\n".join(test_result1))
        output2 = ("\n".join(test_result2))
        output3 = ("\n".join(test_result3))
        output4 = ("\n".join(test_result4))
        self.assertEqual(result1, output1)
        self.assertEqual(result2, output2)
        self.assertEqual(result3, output3)
        self.assertEqual(result4, output4)

        file1.close()
        file2.close()
        file3.close()
        file4.close()

        file1_res.close()
        file2_res.close()
        file3_res.close()
        file4_res.close()

    def test_chopAfterNLines(self):
        splitter = Splitter
        file1 = open(os.path.join(data_path, "TenLinesOneInput.txt"), "r")
        file2 = open(os.path.join(data_path, "TenLinesThreeInput.txt"), "r")
        file3 = open(os.path.join(data_path, "FiftyLinesFiveInput.txt"), "r")
        file4 = open(os.path.join(data_path, "FiftyLinesTwelveInput.txt"), "r")

        file1_res = open(os.path.join(data_path, "TenLinesOneOutput.txt"), "r")
        file2_res = open(os.path.join(data_path, "TenLinesThreeOutput.txt"), "r")
        file3_res = open(os.path.join(data_path, "FiftyLinesFiveOutput.txt"), "r")
        file4_res = open(os.path.join(data_path, "FiftyLinesTwelveOutput.txt"), "r")

        data1 = file1.read()
        data2 = file2.read()
        data3 = file3.read()
        data4 = file4.read()

        result1 = file1_res.read().encode().decode('unicode_escape')
        result2 = file2_res.read().encode().decode('unicode_escape')
        result3 = file3_res.read().encode().decode('unicode_escape')
        result4 = file4_res.read().encode().decode('unicode_escape')

        test_result1 = splitter.chopAfterNLines(data1, 1)
        test_result2 = splitter.chopAfterNLines(data2, 3)
        test_result3 = splitter.chopAfterNLines(data3, 5)
        test_result4 = splitter.chopAfterNLines(data4, 12)

        output1 = ("".join(test_result1))
        output2 = ("".join(test_result2))
        output3 = ("".join(test_result3))
        output4 = ("".join(test_result4))

        self.assertEqual(result1, output1)
        self.assertEqual(result2, output2)
        self.assertEqual(result3, output3)
        self.assertEqual(result4, output4)

        file1.close()
        file2.close()
        file3.close()
        file4.close()

        file1_res.close()
        file2_res.close()
        file3_res.close()
        file4_res.close()