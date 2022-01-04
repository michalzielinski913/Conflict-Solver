import eel

from model.FileInterface import FileInterface


class StandardText(FileInterface):
    def __init__(self, path):
        file = open(path, "r")
        self.text = file.read()



    def getText(self):
        return self.text
