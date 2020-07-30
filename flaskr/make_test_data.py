import json
import student_registration as s

TEST_DIR = "testing-data/"

with open(TEST_DIR + "users.json", 'r') as users_file:
    for user in json.load(users_file):
        s.db.session.add(s.User(id=user["id"], email=user["email"]))

with open(TEST_DIR + "activities.json", 'r') as activities_file:
    for activity in json.load(activities_file):
        s.db.session.add(s.Activity(name=activity["name"]))

s.db.session.commit()
