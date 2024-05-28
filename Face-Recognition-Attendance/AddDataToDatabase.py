import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-f71c3-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "07UW":
        {
            "name": "Mirza Jasmine",
            "major": "ML Engineer",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-04-01 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "36UW":
        {
            "name": "Khushi Gupta",
            "major": "Software Engineer",
            "starting_year": 2021,
            "total_attendance": 4,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-04-01 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)