from model.FileWriterInterface import FileWriterInterface

"""
Implementation of FileWriterInterface supporting basic text files (txt, csv etc.)
"""
class StandardTextWriter(FileWriterInterface):

    def __init__(self, path):
        super().__init__(path)
        self.file = open(path, "w")

    def write_line_to_file(self, line):
        self.file.write(line)
        self.file.flush()

    def finish(self):
        self.file.close()