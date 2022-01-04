from model.Comparator import Comparator
from model.StandardText import StandardText
from model.Splitter import Splitter
import tkinter as tk
from tkinter import filedialog
import eel


class Controler:

    def __init__(self):
        self.splitter = Splitter()
        self.comparator=Comparator()

    def setSplitSettings(self, mode, N):
        self.mode = mode
        self.N = N

    def getSplitSettings(self):
        return self._mode, self._N

    def chooseFilePath(self, wildcard="*"):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def solveConflict(self, id, option, newText):
        eel.removeRow(id)
        eel.setLeftText("")
        eel.setRightText("")
        self.comparator.solveConflict(int(id), option, newText)

    def getFragment(self, id):
        textOne, textTwo = self.comparator.getElement(int(id))
        eel.setLeftText(textOne)
        eel.setRightText(textTwo)

    def cancelCompare(self):
        self.cancel = True
        pass

    def splitFiles(self, dataOne, dataTwo):
        if self.mode == "line":
            partOne = self.splitter.chopAfterNLines(dataOne, self.N)
            partTwo = self.splitter.chopAfterNLines(dataTwo, self.N)
        elif self.mode == "char":
            partOne = self.splitter.chopAfterNChars(dataOne, self.N)
            partTwo = self.splitter.chopAfterNChars(dataTwo, self.N)
        elif self.mode == "word":
            partOne = self.splitter.chopAfterNWords(dataOne, self.N)
            partTwo = self.splitter.chopAfterNWords(dataTwo, self.N)
        elif self.mode == "sentence":
            partOne = self.splitter.chopAfterNSentence(dataOne, self.N)
            partTwo = self.splitter.chopAfterNSentence(dataTwo, self.N)
        return partOne, partTwo

    def loadAndCompare(self, pathOne, pathTwo):
        self.cancel = False
        x=0
        try:
            fileOne = StandardText(pathOne)
        except:
            eel.emergencyCancel()
            eel.sendAlert("File: "+pathOne+"\n Could not be opened!")
            return
        try:
            fileTwo = StandardText(pathTwo)
        except:
            eel.emergencyCancel()
            eel.sendAlert("File: "+pathTwo+"\n Could not be opened!")
            return


        dataOne = fileOne.getText()
        dataTwo = fileTwo.getText()

        partOne, partTwo=self.splitFiles(dataOne, dataTwo)

        for elementOne, elementTwo in zip(partOne, partTwo):
            if self.cancel == True:
                return
            if (x % 1000 == 0):
                eel.addRows(self.comparator.getJson())
                self.comparator.resetJson()
                eel.sleep(0.5)
            self.comparator.compare(elementOne, elementTwo)
            x += 1

        eel.addRows(self.comparator.getJson())
        eel.sendAlert("Comparing complete!", "")
        self.comparator.resetJson()