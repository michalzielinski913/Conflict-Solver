import re
import time

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
        regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
        data = re.split(regex, data)
        data = [' '.join(data[i: i + n]) for i in range(0, len(data), n)]
        return data

    def chopAfterNLines(data, n):
        data = data.splitlines(True)
        data = [' '.join(data[i:i+n]) for i in range(0,len(data),n)]
        return data

# file = open("enwik8", "r")
file = open("długieLoremIpsum2.txt", "r")
data = file.read()
temp = Splitter
start = time.time()
# print(temp.chopAfterNChars(data, 10))
# print(temp.chopAfterNWords(data, 10))
print(temp.chopAfterNSentence(data, 3))
# print(temp.chopAfterNLines(data, 2))
end = time.time()
print(end - start)