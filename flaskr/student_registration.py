from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(
    __name__,
    static_url_path="",
    static_folder="static",
    template_folder="templates"
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

API_PATH = "/api/"


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return "<Activity {}: {}>".format(self.id, self.name)


class User(db.Model):
    id = db.Column(db.Text, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return "<Student {}>".format(self.id)


class Enrollment(db.Model):
    id = db.Column(db.Text, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"))
    user_id = db.Column(db.Text, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Enrollment: user {} in activity {}>".format(self.user_id, self.activity_id)


db.create_all()


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
