import eel
from controller.Controller import Controler
###TODO###
#Input validation
#Notifications about errors/finish in UI
#3rd file generation
#Solve file browser problems (window opens in the background)
# TESTS

eel.init('web')

controller=Controler()

@eel.expose
def getFilePath(wildcard="*"):
    return controller.chooseFilePath()

@eel.expose
def loadAndCompare(pathOne, pathTwo):
    controller.loadAndCompare(pathOne, pathTwo)

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