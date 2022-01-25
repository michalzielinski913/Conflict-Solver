/**
 * This class is responsible for coordinating what happens within GUI
 */
class View{
    /**
     * Class constructor, It initializes class fields
     */
    constructor() {
       this.leftTextPanel=new TextDisplay("textOneContent");
       this.rightTextPanel=new TextDisplay("textTwoContent");
       this.utility=new UtilityDisplay();
       this.list=new DifferenceList();
    }

    /**
     * Set value of left text area
     * @param value Text to display
     */
    setLeftText(value){
        this.leftTextPanel.setText(value);
    }
    /**
     * Set value of right text area
     * @param value Text to display
     */
    setRightText(value){
        this.rightTextPanel.setText(value);
    }

    /**
     * Set path to the first file to compare
     * @param value File path
     */
    setLeftFile(value){
        this.utility.setFirstPath(value);
    }
    /**
     * Set path to the second file to compare
     * @param value File path
     */
    setRightFile(value){
        this.utility.setSecondPath(value);
    }

    /**
     * Append list with new rows
     * @param json JSON formatted string with new elements
     */
    addRows(json){
        this.list.addRows(json);
    }

    /**
     * Get ID of current highlighted element
     * @returns {string}
     */
    getChoosenElement(){
        return this.list.getSelected();
    }

    /**
     * Remove all rows from the table
     */
    clearTable(){
        this.list.clearTable();
    }

    /**
     * Cancel file comparision process
     */
    cancelCompare(){
        eel.cancel_compare();
        this.clearTable();
        document.getElementById("selection").hidden=true;
        document.getElementById("options").hidden=false;
        document.getElementById("thirdFile").hidden=true;
    }

    /**
     * Solve compare conflict of current pair of elements
     */
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

    /**
     * Load files which paths are defined in GUI and begin comparision process
     */
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

    /**
     * Remove specific row from table
     * @param id ID of row which will be removed
     */
    removeRow(id){
        this.list.removeRow(id)
    }

    /**
     * Display notification to the user
     * @param msg Context of notification message
     */
    sendAlert(msg){
        alert(msg);
    }

    /**
     * Generate third file
     */
    generateThirdFile(){
        eel.generate_third_file(document.getElementById("thirdFilePath").value);
    }

    /**
     * Set third file path
     * @param path
     */
    thirdFilePath(path){
        this.utility.setThirdFilePath(path)
    }

}
var viewObject=new View();
/*
 In this project We use EEL library to create application.
 Javascript layer can communicate with Python layer (and vice versa) by so called "exposed" functions
 However We can not expose class methods directly therefore below We have a set of 'friend' functions which wraps methods of View class
 */
eel.expose(setLeftText);
function setLeftText(value) {
    viewObject.setLeftText(value);
}

eel.expose(setRightText);
function setRightText(value) {
    viewObject.setRightText(value);
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

function setThirdFilePath() {
         eel.third_file_path()(function(path){
        viewObject.thirdFilePath(path);

    }) }
function setLeftFile() {
         eel.get_file_path()(function(path){
        viewObject.setLeftFile(path);

    }) }
function setRightFile() {
         eel.get_file_path()(function(path){
        viewObject.setRightFile(path);

    })
}
