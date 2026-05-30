from fastapi import FastAPI
import json

app = FastAPI()

FILE_NAME = "courses.json"


def load_courses():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_courses(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


@app.get("/")
def home():
    return {"message": "FastAPI is running!"}


@app.get("/courses")
def get_courses():
    return load_courses()


@app.post("/courses")
def add_course(course: dict):
    courses = load_courses()
    courses.append(course)
    save_courses(courses)
    return {
        "message": "course added",
        "course": course
    }