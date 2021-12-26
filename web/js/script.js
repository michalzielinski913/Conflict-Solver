$("#table tr").click(function(){
        $(this).addClass('selected').siblings().removeClass('selected');

   });

function selectFile(box) {

     eel.pythonFunction()(function(path){
    // Update the div with a random number returned by python
    document.getElementById(box).value = path;

    })
      };
function testFile() {
     if (document.getElementById('fileOnePath').value == '' || document.getElementById('fileTwoPath').value == '') {
         return;
     }
     viewObject.clearTable();
     document.getElementById('textOneContent').contentEditable = true;
     document.getElementById('textOneContent').innerHTML = "";
     eel.loadFile(document.getElementById('fileOnePath').value, document.getElementById('fileTwoPath').value);
     document.getElementById("options").hidden = true;
     document.getElementById("selection").hidden = false;
 };

 eel.expose(append_text_one);
 function append_text_one(line) {
     var selectionStart = $('#textTwoContent')[0].selectionStart;
var selectionEnd = $('#textTwoContent')[0].selectionEnd;

$('#textTwoContent').val($('#textTwoContent').val() + line);

$('#textTwoContent')[0].selectionStart = selectionStart;
$('#textTwoContent')[0].selectionEnd = selectionEnd;

 }
 
 function cancelCompare() {
            viewObject.clearTable();
          document.getElementById("selection").hidden=true;
         document.getElementById("options").hidden=false;
 }