from flask import Flask, request

app = Flask(
    __name__,
    static_url_path="",
    static_folder="static",
    template_folder="templates"
)
API_PATH = "/api/"

@app.route("/")
def landing_page():
    return app.send_static_file("index.html")

@app.route(API_PATH + "activities/", methods=["GET", "POST"])
def activities():
    if request.method == "POST":
        return "I don't know how to make activities"
    else:
        return "activities"

@app.route(API_PATH + "activities/<int:id>", methods=["GET", "PUT", "DELETE"])
def activity(id):
    if request.method == "PUT":
        return "I don't know how to change activities"
    elif request.method == "DELETE":
        return "I don't know how to delete activities"
    else:
        return "activity"

@app.route(API_PATH + "enroll")
def enroll():
    return "RIP"
