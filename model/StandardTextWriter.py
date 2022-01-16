from model.FileWriterInterface import FileWriterInterface


class StandardTextWriter(FileWriterInterface):

    def __init__(self, path):
        super().__init__(path)
        self.file = open(path, "w")

    def write_line_to_file(self, line):
        self.file.write(line)
        self.file.flush()
