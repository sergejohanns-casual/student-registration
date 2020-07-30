const API_ENROLL = window.location.origin + "/api/enroll/";

function submitResults() {
    submitButton.disabled = true;
    userId = document.getElementById("user-id").value;
    activityId = document.getElementById("activity-id").value;
    form = document.getElementById("form");
    errorMessage = document.getElementById("error-message");

    console.log("making request");
    request = new XMLHttpRequest();
    request.open("POST", API_ENROLL);
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.onreadystatechange = function() {
        console.log("Changed to " + this.readyState);
        if (this.readyState === XMLHttpRequest.DONE) {
            console.log("Done: " + this.status);
            if (this.status === 204) {
                form.innerHTML = "Your enrollment was processed correctly. You have been sent an email with which you can confirm your enrollment.";
            } else if (this.status === 422) {
                errorMessage.innerHTML = "That username or activity is not know to us.";
                submitButton.disabled = false;
            }
        }
    };
    console.log(JSON.stringify({"user": userId, "activity": activityId}));
    request.send(JSON.stringify({"user": userId, "activity": activityId}));
}

submitButton = document.getElementById("submit");
submitButton.addEventListener("click", submitResults);
