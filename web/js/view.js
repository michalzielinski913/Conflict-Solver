
class View{
    constructor() {
       this.leftTextPanel=new TextDisplay("textOneContent");
       this.rightTextPanel=new TextDisplay("textTwoContent");
       this.utility=new UtilityDisplay();
       this.list=new DifferenceList();
    }

    setLeftText(value){
        this.leftTextPanel.setText(value);
    }

    setRightText(value){
        this.rightTextPanel.setText(value);
    }

    setLeftFile(value){
        this.utility.setFirstPath(value);
    }

    setRightFile(value){
        this.utility.setSecondPath(value);
    }

    getLeftFile(){
        return this.utility.getFirstPath();
    }
    getRightFile(){
        return this.utility.getSecondPath();
    }

    addRow(leftText, rightText, id){
        this.list.addRow(leftText, rightText, id);
    }

    getChoosenElement(){
        return this.list.getSelected();
    }

}
var viewObject=new View();
eel.expose(setLeftText);
function setLeftText(value) {
    viewObject.setLeftText(value);
}

eel.expose(setRightText);
function setRightText(value) {
    viewObject.setRightText(value);
}

function setLeftFile() {
         eel.getFilePath()(function(path){
        viewObject.setLeftFile(path);

    })

}

function setRightFile() {
         eel.getFilePath()(function(path){
    // Update the div with a random number returned by python
    viewObject.setRightFile(path);

    })

}

