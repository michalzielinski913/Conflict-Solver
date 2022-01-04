
class Comparator:
    def __init__(self):
        self.dictionary = {}
        self.x = 1
        self.json=""

    def compare(self, elementOne, elementTwo):
        row = [elementOne, elementTwo]
        self.dictionary[self.x] = row
        if elementOne!=elementTwo:
            self.addElement(elementOne, elementTwo)
        self.x += 1


    def addElement(self, elementOne, elementTwo):
        line1 = elementOne.replace("\'", "\"")
        line2 = elementTwo.replace("\'", "\"")
        jsonElement = {
            "DT_RowId": self.x,
            "FirstFile": line1[:33],
            "SecondFile": line2[:33]
        }
        self.json = self.json + str(jsonElement) + ","

    def getJson(self):
        self.json = self.json[:-1]
        self.json = self.json.replace("\"", "\\\"")
        self.json = self.json.replace("\'", "\"")
        self.json = "[" + self.json + "]"
        return self.json

    def resetJson(self):
        self.json=""

    def getElement(self, id):
        return self.dictionary[id]

    def solveConflict(self, id, option, newText):
        if(option=="textOne"):
            return
        elif(option=="textTwo"):
            self.dictionary[id][0]=self.dictionary[id][1]
        elif(option=="custom"):
            self.dictionary[id][0]=newText

    def getFirstColumn(self):
        for i in range(len(self.dictionary)):
            yield self.dictionary[i+1][0]