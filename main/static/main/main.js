function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
  
  function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
  
function checkCookie() {
    let user = getCookie("new_cust");
    if (user != "") {
        checkNewCustomerCookie();
    } else {        
        setCookie("new_cust", '1', 365);      
    }
  }

function checkNewCustomerCookie() {
    // Get all cookies and split them into an array
    var cookies = document.cookie.split(';');    
    // Iterate through the cookies to find 'new_cust' with value '1'
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        console.log(cookie);
        // Check if the cookie is 'new_cust' with value '1'
        if (cookie.startsWith('new_cust=1')) {
            // Remove the form from the document
            console.log("this should run");
            var form = document.getElementById('emailForm'); 
            
            if (form) {
                form.remove();
            }
            break;
        }
    }
}

window.onload = function() {
    // checkNewCustomerCookie();
    console.log("form");
};

