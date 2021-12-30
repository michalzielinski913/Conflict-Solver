from controller.splitter import Splitter
from model.txtFile import txtFile
import tkinter as tk
from tkinter import filedialog
import eel


class Controler:

    def __init__(self):
        self.splitter = Splitter()

    def setSplitSettings(self, mode, N):
        self._mode = mode
        self._N = N

    def getSplitSettings(self):
        return self._mode, self._N

    def loadFiles(self, pathOne, pathTwo):
        self.fileOne = txtFile(pathOne)
        self.fileTwo = txtFile(pathTwo)

    def chooseFilePath(self, wildcard="*"):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def solveConflict(self, id, option, newText=None):
        eel.removeRow(id)
        eel.setLeftText("")
        eel.setRightText("")
        pass

    def getFragment(self, id):
        eel.setLeftText(self.dictT[int(id)][0])
        eel.setRightText(self.dictT[int(id)][1])

    def cancelCompare(self):
        self.cancel = True
        pass

    def loadFiles(self, pathOne, pathTwo):
        self.dictT = {}
        self.cancel = False
        x = 1
        jsonS = ""
        jsonElements = []
        fileOne = open(pathOne, "r")
        fileTwo = open(pathTwo, "r")
        dataOne = fileOne.read()
        dataTwo = fileTwo.read()

        if self._mode == "line":
            partOne = self.splitter.chopAfterNLines(dataOne, self._N)
            partTwo = self.splitter.chopAfterNLines(dataTwo, self._N)
        elif self._mode == "char":
            partOne = self.splitter.chopAfterNChars(dataOne, self._N)
            partTwo = self.splitter.chopAfterNChars(dataTwo, self._N)
        elif self._mode == "word":
            partOne = self.splitter.chopAfterNWords(dataOne, self._N)
            partTwo = self.splitter.chopAfterNWords(dataTwo, self._N)
        elif self._mode == "sentence":
            partOne = self.splitter.chopAfterNSentence(dataOne, self._N)
            partTwo = self.splitter.chopAfterNSentence(dataTwo, self._N)

        for elementOne, elementTwo in zip(partOne, partTwo):
            if self.cancel == True:
                return
            if (x % 1000 == 0):
                jsonS = jsonS[:-1]
                jsonS = jsonS.replace("\"", "\\\"")
                jsonS = jsonS.replace("\'", "\"")
                jsonS = "[" + jsonS + "]"
                eel.addRows(jsonS)
                eel.sleep(0.5)
                jsonS = ""
            line1 = elementOne.replace("\'", "\"")
            line2 = elementTwo.replace("\'", "\"")
            jsonElement = {
                "DT_RowId": x,
                "FirstFile": line1[:33],
                "SecondFile": line2[:33]
            }
            jsonS = jsonS + str(jsonElement) + ","
            row = [line1, line2]
            self.dictT[x] = row
            x += 1

        for element in jsonElements:
            jsonS = jsonS + str(element) + ","

        jsonS = jsonS[:-1]
        jsonS = jsonS.replace("\"", "\\\"")
        jsonS = jsonS.replace("\'", "\"")
        jsonS = "[" + jsonS + "]"
        jsonElements = []
        eel.addRows(jsonS)