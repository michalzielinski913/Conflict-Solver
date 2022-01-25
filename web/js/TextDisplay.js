/**
 * Class which represents text field used for displaying element
 */
class TextDisplay{
    /**
     * Class constructor, It initializes class fields
     * @param id ID of text area to which class will be bounded
     */
    constructor(id) {
        this.id=id;
        this.object=document.getElementById(id);
    }

    /**
     * Get text which is currently in the textarea
     * @returns {string} text inside textarea
     */
    getText(){
        return document.getElementById(this.id).value;
    }

    /**
     * Set context of given textarea
     * @param {string} Text which will be displayed inside textarea
     */
    setText(value){
        document.getElementById(this.id).value=value;
    }

}