from model.txtFile import txtFile
import tkinter as tk
from tkinter import filedialog

class Controler:

    def __init__(self):
        pass

    def setSplitSettings(self, mode, N):
        self._mode=mode
        self._N=N

    def getSplitSettings(self):
        return self._mode, self._N

    def loadFiles(self, pathOne, pathTwo):
        self.fileOne=txtFile(pathOne)
        self.fileTwo=txtFile(pathTwo)

    def chooseFilePath(self, wildcard="*"):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def solveConflict(self, id, option, newText=None):
        pass

    def getFragment(self, id):
        pass