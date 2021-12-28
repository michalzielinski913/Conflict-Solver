from model.txtFile import txtFile
import tkinter as tk
from tkinter import filedialog
import eel
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
        eel.removeRow(id)
        eel.setLeftText("")
        eel.setRightText("")
        pass

    def getFragment(self, id):
        eel.setLeftText(self.dictT[int(id)][0])
        eel.setRightText(self.dictT[int(id)][1])


    def cancelCompare(self):
        self.cancel=True
        pass


    def loadFiles(self, pathOne, pathTwo):
        print(pathOne)
        print(pathTwo)
        self.dictT = {}
        self.cancel=False
        x = 1
        jsonS = ""
        jsonElements = []
        with open(pathOne) as file1, open(pathTwo) as file2:
            for line1, line2 in zip(file1, file2):
                if self.cancel==True:
                    return
                if (x % 1000 == 0):
                    jsonS = jsonS[:-1]
                    jsonS = jsonS.replace("\"", "\\\"")
                    jsonS = jsonS.replace("\'", "\"")
                    jsonS = "[" + jsonS + "]"
                    eel.addRows(jsonS)
                    eel.sleep(0.5)
                    jsonS = ""
                line1 = line1.replace("\'", "\"")
                line2 = line2.replace("\'", "\"")
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