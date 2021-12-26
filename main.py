import eel
from test import test
import wx
from model.txtFile import txtFile
from controller.Controller import Controler
import tkinter as tk
from tkinter import filedialog
import json

eel.init('web')

controller=Controler()

@eel.expose
def getFilePath(wildcard="*"):
    return controller.chooseFilePath()
dictT={}


@eel.expose
def loadFile(pathOne, pathTwo):
    print(pathOne)
    print(pathTwo)

    x = 1
    jsonS = ""
    jsonElements=[]
    with open(pathOne) as file1, open(pathTwo) as file2:
        for line1, line2 in zip(file1, file2):
            if(x%2000==0):
                jsonS=jsonS[:-1]
                jsonS = jsonS.replace("\"", "\\\"")
                jsonS = jsonS.replace("\'", "\"")
                jsonS="["+jsonS+"]"
                eel.addRows(jsonS)
                eel.sleep(0.5)
                jsonS = ""
            line1 = line1.replace("\'", "\"")
            line2 = line2.replace("\'", "\"")
            jsonElement={
                "DT_RowId": x,
                "FirstFile": line1[:33],
                "SecondFile": line2[:33]
            }
            jsonS = jsonS + str(jsonElement) + ","
            row = [line1, line2]
            dictT[x] = row
            x += 1

        for element in jsonElements:
            jsonS = jsonS + str(element) + ","

        jsonS = jsonS[:-1]
        jsonS = jsonS.replace("\"", "\\\"")
        jsonS = jsonS.replace("\'", "\"")
        jsonS = "[" + jsonS + "]"
        jsonElements = []
        eel.addRows(jsonS)

#C:/Users/Michał/Downloads/Tkinter-Designer-1.0.4/requirements.txt

@eel.expose
def getFragment(id):
    eel.setLeftText(dictT[int(id)][0])
    eel.setRightText(dictT[int(id)][1])


@eel.expose
def solveConflict(id, option, newText=None):
    controller.solveConflict(id, option, newText)

@eel.expose
def setSplitSettings(mode, N):
    controller.setSplitSettings(mode, N)

eel.start('main.html')