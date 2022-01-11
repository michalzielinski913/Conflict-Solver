import re
import time
import os

class Splitter:
    def chopAfterNChars(data, n):
        regex = ".{1," + str(n) + "}"
        data = data.replace('\n', '')
        data = re.findall(regex, data)
        return data

    def chopAfterNWords(data, n):
        data = data.split()
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chopAfterNSentence(data, n):
        regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
        data = re.split(regex, data)
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chopAfterNLines(data, n):
        data = data.splitlines(True)
        data = [''.join(data[i:i+n]) for i in range(0,len(data),n)]
        return data


DATA = os.path.join(os.path.dirname(__file__), 'test_data')
data_path = os.path.dirname(__file__)
print(DATA)
print(data_path)



