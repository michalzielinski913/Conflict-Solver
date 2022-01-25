/**
 * DifferenceList class represents table which hold different pairs of elements
 */
class DifferenceList{
    /**
     * Class constructor, It initializes class fields
     */
    constructor() {
        this.tabID="differenceTab"
    }

    /**
     * This method add additional rows to the table
     * @param json JSON formatted list of new elements
     */
    addRows(json){
        var t =$('#'+this.tabID).DataTable();
        var elements = JSON.parse(json);

        t.rows.add(elements).draw();
    }

    /**
     * Return ID of element which is currently highlighted
     * @returns {string} ID of highlighted element
     */
    getSelected(){
        return document.getElementsByClassName("selected")[0].id;
    }

    /**
     * Removes all rows from table
     */
    clearTable(){
        var t =$('#'+this.tabID).DataTable();
        t.clear().draw();

    }

    /**
     * Remove row with specific ID
     * @param id ID of row which will be removed
     */
    removeRow(id){
        var t =$('#'+this.tabID).DataTable();
        t.row('#'+id).remove().draw();

    }

    /**
     * Return amount of rows in table
     * @returns {integer} Amount of rows in table
     */
    getRowsAmount(){
        var t =$('#'+this.tabID).DataTable();
        return  t.data().count();
    }


}