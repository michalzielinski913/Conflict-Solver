from model.FileWriterInterface import FileWriterInterface


class StandardTextWriter(FileWriterInterface):

    def __init__(self, path):
        self.file = open(path, "w")

    def writeLineToFile(self, line):
        self.file.write(line)
        self.file.flush()

    def finish(self):
        self.file.close()