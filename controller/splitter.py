import re

class Splitter:
    def chopAfterNChars(data, n):
        regex = ".{1," + str(n) + "}"
        print(regex)
        data = re.findall(regex, data)
        return data

    def chopAfterNWords(data, n):
        data = data.split()
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chopAfterNSentence(data, n):
        regex = ".*[!?.]{1," + str(n) + "}"
        data = re.findall(regex, data)
        return data

    def chopAfterNLines(data, n):
        data = data.splitlines(True)
        data = [' '.join(data[i:i+n]) for i in range(0,len(data),n)]
        return data