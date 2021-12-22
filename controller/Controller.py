from model.txtFile import txtFile


class Controler:

    def __init__(self):
        pass

    def loadFiles(self, pathOne, pathTwo):
        self.fileOne=txtFile(pathOne)
        self.fileTwo=txtFile(pathTwo)