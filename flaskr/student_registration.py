import json
import http
import secrets
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, UnprocessableEntity


app = Flask(
    __name__,
    static_url_path="",
    static_folder="static",
    template_folder="templates"
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

API_PATH = "/api/"
CREDENTIALS_FILE = "credentials.json"
with open(CREDENTIALS_FILE, 'r') as cred_file:
    data = json.load(cred_file)
    EMAIL_CLIENT = data["client"]
    EMAIL_PORT = data["port"]
    SENDER_ADDRESS = data["address"]
    SENDER_PASSWORD = data["password"]


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)


class User(db.Model):
    id = db.Column(db.Text, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)


class TempEnrollment(db.Model):
    id = db.Column(db.Text, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"))
    user_id = db.Column(db.Text, db.ForeignKey("user.id"))


class Enrollment(db.Model):
    id = db.Column(db.Text, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"))
    user_id = db.Column(db.Text, db.ForeignKey("user.id"))


db.create_all()


def gen_key(user, activity):
    while True:
        res = secrets.token_urlsafe(32)
        if Enrollment.query.filter_by(id=res).first() is None and TempEnrollment.query.filter_by(id=res).first() is None:
            return res


@app.route("/")
def index_page():
    return app.send_static_file("index.html")


@app.route(API_PATH + "enroll/", methods=["POST"])
def enroll():
    data = request.json
    if data is None:
        raise BadRequest
    elif "user" not in data or "activity" not in data:
        raise UnprocessableEntity
    uid, aid = data["user"], data["activity"]
    user = User.query.filter_by(id=uid).first()
    activity = Activity.query.filter_by(id=aid).first()
    if user is None or activity is None:
        raise UnprocessableEntity
    db.session.add(TempEnrollment(id=gen_key(user, activity), user_id=user.id, activity_id=activity.id))
    db.session.commit()
    return '', http.HTTPStatus.NO_CONTENT


@app.route(API_PATH + "enroll/<key>", methods=["POST"])
def confirm_enroll():
    temp = TempEnrollment.query.filter_by(id=request.args.get("key")).first_or_404()
    db.session.remove(temp)
    db.session.add(Enrollment(id=temp.id, user_id=temp.user_id, activity_id=temp.activity_id))
    db.session.commit()
    return '', http.HTTPStatus.NO_CONTENT
