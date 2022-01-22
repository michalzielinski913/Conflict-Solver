
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

    addRow(table){
        for (const element of table) {
            this.list.addRow(element[0], element[1], element[2]);

        }
    }

    addRows(json){
        this.list.addRows(json);
    }

    getChoosenElement(){
        return this.list.getSelected();
    }

    clearTable(){
        this.list.clearTable();
    }

    cancelCompare(){
        eel.cancel_compare();
        this.clearTable();
        document.getElementById("selection").hidden=true;
        document.getElementById("options").hidden=false;
        document.getElementById("thirdFile").hidden=true;
    }

    solveCompare(){
        try{
            eel.solve_conflict(this.getChoosenElement(), $('input[name="conflictOption"]:checked').val(), $('textarea[name="thirdOptionValue"]').val());

        }catch (e) {
            return;
        }
        if(this.list.getRowsAmount()==1){
            document.getElementById("selection").hidden=true;
            document.getElementById("options").hidden=true;
            document.getElementById("thirdFile").hidden=false;
        }
    }

    loadAndCompare(){
        try{
            eel.set_split_settings($('input[name="mode"]:checked').val(), parseInt(document.getElementById("N").value))
         if (document.getElementById('fileOnePath').value == '' || document.getElementById('fileTwoPath').value == '') {
             return;
         }
         this.clearTable();
         document.getElementById('textOneContent').contentEditable = true;
         document.getElementById('textOneContent').innerHTML = "";
         eel.load_and_compare(document.getElementById('fileOnePath').value, document.getElementById('fileTwoPath').value);
         document.getElementById("options").hidden = true;
         document.getElementById("selection").hidden = false;
         document.getElementById("thirdFile").hidden=true;
        }catch (e) {
            return;
        }

    }

    removeRow(id){
        this.list.removeRow(id)
    }

    sendAlert(msg){
        alert(msg);
    }
    generateThirdFile(){
        eel.generate_third_file(document.getElementById("thirdFilePath").value);
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

eel.expose(addRow)
function addRow(leftElement, rightElement, id) {
    viewObject.addRow(leftElement, rightElement, id);
}

eel.expose(addRows)
function addRows(json) {
    viewObject.addRows(json)
}

eel.expose(removeRow)
function removeRow(id){
    viewObject.removeRow(id);
}

eel.expose(sendAlert)
function sendAlert(msg){
    viewObject.sendAlert(msg);
}

eel.expose(cancelCompare)
function cancelCompare(){
    viewObject.cancelCompare();
}
function setLeftFile() {
         eel.get_file_path()(function(path){
        viewObject.setLeftFile(path);

    }) }
function setRightFile() {
         eel.get_file_path()(function(path){
        viewObject.setRightFile(path);

    })
}
