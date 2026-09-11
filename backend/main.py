import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for Angular frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

JSON_FILE = "student_data.json"
DASHBOARD_FILE = "dashboard_data.json"

# Read or load data from the JSON file
def load_student_data():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as file:
        return json.load(file)

# Updated data of the Json
def save_student_data(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)


# 1. Get List of Students Endpoint
@app.get("/students_list")
def getStudents():
    students_db = load_student_data()
    return students_db


# 2. View Single Student Endpoint
@app.get("/student-view/{student_id}")
def viewStudent(student_id: int):
    students_db = load_student_data()
    for stu in students_db:
        if stu["id"] == student_id:
            return stu
    raise HTTPException(status_code=404, detail="Kindly search for the valid student")


# 3. Delete Student Endpoint
@app.delete("/students_delete/{student_id}")
def delete_student(student_id: int):
    students_db = load_student_data()
    
    for index, stu in enumerate(students_db):
        if stu["id"] == student_id:
            deleted_student = students_db.pop(index)
            save_student_data(students_db)
            return {
                "message": f"Student with ID {student_id} deleted successfully",
                "data": deleted_student,
            }
            
    raise HTTPException(status_code=404, detail="Student not found")

@app.get("/student_dashboard")
def get_dashboard_data():
    if not os.path.exists(DASHBOARD_FILE):
        raise HTTPException(status_code=404, detail="Dashboard data file not found")
        
    with open(DASHBOARD_FILE, "r") as file:
        data = json.load(file)
        
    return data