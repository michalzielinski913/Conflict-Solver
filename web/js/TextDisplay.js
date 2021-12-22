class TextDisplay{
    constructor(id) {
        this.id=id;
        this.object=document.getElementById(id);
    }

    getText(){
        return document.getElementById(this.id).value;
    }

    setText(value){
        document.getElementById(this.id).value=value;
    }

}