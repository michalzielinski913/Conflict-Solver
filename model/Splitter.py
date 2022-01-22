import re
import time
import os

"""
Splitter class responsible for splitting text to chunks with parameters defined by user
"""
class Splitter:
    def chop_after_n_chars(self, data, n):
        """
        Split text to chunks with size of n characters
        :param data: Text to be splitted
        :param n: chunk size
        :return: Array where each elements contains n characters
        """
        regex = '.{1,' + str(n) + '}'
        print(regex)
        data = re.findall(regex, data)
        return data

    def chop_after_n_words(self, data, n):
        """
        Split text to chunks with size of n words
        :param data: Text to be splitted
        :param n: chunk size
        :return: Array where each elements contains n words
        """
        data = data.split()
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chop_after_n_sentence(self, data, n):
        """
        Split text to chunks with size of n sentences
        :param data: Text to be splitted
        :param n: chunk size
        :return: Array where each elements contains n sentences
        """
        regex = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
        data = re.split(regex, data)
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chop_after_n_lines(self, data, n):
        """
        Split text to chunks with size of n lines
        :param data: Text to be splitted
        :param n: chunk size
        :return: Array where each elements contains n lines
        """
        data = data.splitlines(True)
        data = [' '.join(data[i:i+n]) for i in range(0, len(data), n)]
        return data