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

@eel.expose
def loadFile(pathOne, pathTwo):
    controller.loadFiles(pathOne, pathTwo)

#C:/Users/Michał/Downloads/długieLoremIpsum2.txt

@eel.expose
def getFragment(id):
    controller.getFragment(id)


@eel.expose
def solveConflict(id, option, newText=None):
    controller.solveConflict(id, option, newText)

@eel.expose
def setSplitSettings(mode, N):
    controller.setSplitSettings(mode, N)

@eel.expose
def cancelCompare():
    controller.cancelCompare()

eel.start('main.html')