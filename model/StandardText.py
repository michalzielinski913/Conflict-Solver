import eel

from model.FileInterface import FileInterface


class StandardText(FileInterface):
    def __init__(self, path):
        super().__init__(path)
        file = open(path, "r")
        self.text = file.read()

    def get_text(self):
        return self.text
