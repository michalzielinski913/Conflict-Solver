class DifferenceList{
    constructor() {
        this.tabID="differenceTab"
    }
    addRow(leftText, rightText, elementID){
        var t =$('#'+this.tabID).DataTable();
        t.row.add([leftText, rightText]).draw(true).node().id=elementID;
    }

    getSelected(){
        return document.getElementsByClassName("selected")[0].id;
    }


}