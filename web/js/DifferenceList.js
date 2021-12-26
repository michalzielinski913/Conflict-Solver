class DifferenceList{
    constructor() {
        this.tabID="differenceTab"
    }
    addRow(leftText, rightText, elementID){
        var t =$('#'+this.tabID).DataTable();
        var persons = JSON.parse("[" +
            "  {" +
            '    "DT_RowId": 1,' +
            '    "FirstFile": "LanTest101",' +
            '    "SecondFile": "x1"' +
            "  }" +
            "]")

        t.rows.add(persons).draw();
    }

    addRows(json){
        var t =$('#'+this.tabID).DataTable();
        var elements = JSON.parse(json);

        t.rows.add(elements).draw();
    }

    getSelected(){
        return document.getElementsByClassName("selected")[0].id;
    }

    clearTable(){
        var t =$('#'+this.tabID).DataTable();
        t.clear().draw();

    }


}