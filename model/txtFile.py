from model.FileInterface import File


class txtFile(File):

    def loadFile(self, path):
        self.text=""
        self.path=path


    def loadText(self):
        with open(self.path, encoding="utf-8") as f:
            x=0
            for line in f.readlines():
                x+=1
                if(x%1000==0):
                    print(x)
                self.text+=line

    def getText(self):
        return self.text

    def getPath(self):
        return self.path