class DifferenceList{
    constructor() {
        this.tabID="differenceTab"
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

    removeRow(id){
        var t =$('#'+this.tabID).DataTable();
        t.row('#'+id).remove().draw();

    }


}