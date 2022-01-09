import eel
from test import test
from model.txtFile import txtFile
import tkinter as tk
from tkinter import filedialog

eel.init('web')

file=txtFile()

@eel.expose
def getFilePath(wildcard="*"):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


@eel.expose
def loadFile(pathOne, pathTwo):
    print(pathOne)
    print(pathTwo)



@eel.expose
def getFragment(id):
    print(id)
    eel.setLeftText("test")
    eel.setRightText("test2")


eel.start('main2.html')