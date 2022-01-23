class UtilityDisplay{

    constructor() {
        this.fileOnePathID="fileOnePath";
        this.fileTwoPathID="fileTwoPath";
        this.mode="FileSelection"
    }

    setFirstPath(value){
        document.getElementById(this.fileOnePathID).value=value;
    }

    setSecondPath(value){
        document.getElementById(this.fileTwoPathID).value=value;
    }

    getFirstPath(){
        return document.getElementById(this.fileOnePathID).value;
    }
    getSecondPath(){
        return document.getElementById(this.fileTwoPathID).value;
    }

    setThirdFilePath(path){
        document.getElementById("thirdFilePath").value=path;
    }

    toggleMode(){
        if(this.mode=="fileSelection"){
            this.mode="conflictOptions";
        }else{
            this.mode="fileSelection";
        }
    }


}