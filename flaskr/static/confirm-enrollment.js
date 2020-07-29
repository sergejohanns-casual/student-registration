const queryParamString = window.location.search;
const urlParams = new URLSearchParams(queryParamString);
const API_CONFIRM_ENROLL = window.location.origin + "/api/enroll/";
const textField = document.getElementById("result");

if (urlParams.has("key")) {
    const request = new XMLHttpRequest();
    request.open("POST", API_CONFIRM_ENROLL + urlParams.get("key"));
    request.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE) {
            if (this.status === 204) {
                textField.innerHTML = "Your enrollment was confirmed succesfully.";
            } else {
                console.log("Unexpected response code: " + this.status);
                textField.innerHTML = "An error occured while confirming your enrollment.";
            }
        }
    };
    request.send();
} else {
    textField.innerHTML = "This page expects a url parameter 'key' but no such parameter is present. If you were redirected to this page by the confirmation email consider contacting the system administrator.";
}
