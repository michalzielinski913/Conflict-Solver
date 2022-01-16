import re
import time
import os


class Splitter:
    def chop_after_n_chars(self, data, n):
        regex = '.{1,' + str(n) + '}'
        print(regex)
        data = re.findall(regex, data)
        return data

    def chop_after_n_words(self, data, n):
        data = data.split()
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chop_after_n_sentence(self, data, n):
        regex = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
        data = re.split(regex, data)
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chop_after_n_lines(self, data, n):
        data = data.splitlines(True)
        data = [' '.join(data[i:i+n]) for i in range(0, len(data), n)]
        return data


data = os.path.join(os.path.dirname(__file__), 'test_data')
data_path = os.path.dirname(__file__)
print(data)
print(data_path)
