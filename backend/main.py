from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Feedback
import json, os

app = FastAPI(title="EduVoice API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FILE = "feedback.json"

def read_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.get("/")
def home():
    return {"message": "EduVoice Backend Running"}

@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    data = read_data()
    data.append(feedback.dict())
    write_data(data)
    return {"message": "Thank you for your feedback!"}

@app.get("/admin/feedback")
def admin_feedback():
    return read_data()
