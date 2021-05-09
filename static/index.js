

//  Disable Refresh
//this code handles the F5/Ctrl+F5/Ctrl+R
// document.onkeydown = function () {
//     switch (event.keyCode) {
//         case 116: //F5 button
//             event.returnValue = false;
//             event.keyCode = 0;
//             return false;
//         case 82: //R button
//             if (event.ctrlKey) {
//                 event.returnValue = false;
//                 event.keyCode = 0;
//                 return false;
//             }
//     }

//////////////////////////////////////////////////////////////////////////////
document.onkeydown = function(e) {
  if(event.keyCode == 123) {
  return false;
  }
  if(e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)){
  return false;
  }
  if(e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)){
  return false;
  }
  if(e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)){
  return false;
  }
  }
  

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// inspect
document.addEventListener('keydown', function () {
    if (event.keyCode == 123) {
        alert("This function has been disabled to prevent you from stealing my code!");
        return false;
    } else if (event.ctrlKey && event.shiftKey && event.keyCode == 73) {
        alert("This function has been disabled to prevent you from stealing my code!");
        return false;
    } else if (event.ctrlKey && event.keyCode == 85) {
        alert("This function has been disabled to prevent you from stealing my code!");
        return false;
    }
}, false);

if (document.addEventListener) {
    document.addEventListener('contextmenu', function (e) {
        alert("This function has been disabled to prevent you from stealing my code!");
        e.preventDefault();
    }, false);
} else {
    document.attachEvent('oncontextmenu', function () {
        alert("This function has been disabled to prevent you from stealing my code!");
        window.event.returnValue = false;
    });
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//disable back button

(function (global) {

    if (typeof (global) === "undefined") {
      throw new Error("window is undefined");
    }

    var _hash = "!";
    var noBackPlease = function () {
      global.location.href += "#";

      // Making sure we have the fruit available for juice (^__^)
      global.setTimeout(function () {
        global.location.href += "!";
      }, 50);
    };

    global.onhashchange = function () {
      if (global.location.hash !== _hash) {
        global.location.hash = _hash;
      }
    };

    global.onload = function () {
      noBackPlease();

      // Disables backspace on page except on input fields and textarea..
      document.body.onkeydown = function (e) {
        var elm = e.target.nodeName.toLowerCase();
        if (e.which === 8 && (elm !== 'input' && elm !== 'textarea')) {
          e.preventDefault();
        }
        // Stopping the event bubbling up the DOM tree...
        e.stopPropagation();
      };
    }
  })(window);