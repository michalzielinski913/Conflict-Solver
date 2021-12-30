import re
import time

class Splitter:
    def chopAfterNChars(self, data, n):
        regex = ".{1," + str(n) + "}"
        print(regex)
        data = re.findall(regex, data)
        return data

    def chopAfterNWords(self, data, n):
        data = data.split()
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chopAfterNSentence(self, data, n):
        regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
        data = re.split(regex, data)
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chopAfterNLines(self, data, n):
        data = data.splitlines(True)
        data = [' '.join(data[i:i+n]) for i in range(0,len(data),n)]
        return data
