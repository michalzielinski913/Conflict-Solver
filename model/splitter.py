import re
import time
import os

class Splitter:
    def chop_after_n_chars(data, n):
        regex = ".{1," + str(n) + "}"
        data = data.replace('\n', '')
        data = re.findall(regex, data)
        return data

    def chop_after_n_words(data, n):
        data = data.split()
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chop_after_n_sentence(data, n):
        regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
        data = re.split(regex, data)
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chop_after_n_lines(data, n):
        data = data.splitlines(True)
        data = [''.join(data[i:i+n]) for i in range(0,len(data),n)]
        return data


DATA = os.path.join(os.path.dirname(__file__), 'test_data')
data_path = os.path.dirname(__file__)
print(DATA)
print(data_path)



