/**
 * This class is responsible for GUI area which holds user controlls (input fields, buttons etc.)
 */
class UtilityDisplay{
    /**
     * Class constructor, It initializes class fields
     */
    constructor() {
        this.fileOnePathID="fileOnePath";
        this.fileTwoPathID="fileTwoPath";
        this.mode="FileSelection"
    }

    /**
     * Set path of first file to compare
     * @param value Path to the file
     */
    setFirstPath(value){
        document.getElementById(this.fileOnePathID).value=value;
    }

    /**
     * Set path of second file to compare
     * @param value Path to the file
     */
    setSecondPath(value){
        document.getElementById(this.fileTwoPathID).value=value;
    }

    /**
     * Get path to the first file
     * @returns {string} Path to the file
     */
    getFirstPath(){
        return document.getElementById(this.fileOnePathID).value;
    }

    /**
     * Get path to the second file
     * @returns {string} Path to the file
     */
    getSecondPath(){
        return document.getElementById(this.fileTwoPathID).value;
    }

    /**
     * Set path to the third file generation
     * @returns {string} Path to the file
     */
    setThirdFilePath(path){
        document.getElementById("thirdFilePath").value=path;
    }

}