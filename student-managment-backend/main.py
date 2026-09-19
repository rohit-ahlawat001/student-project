import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import date, datetime
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
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

class CreateStudent(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2, example="Rohit Kumar")
    course: str = Field(..., example="Computer Science")
    semester: int = Field(..., gt=0, description="Semester must be greater than 0")
    fee_paid_amount: float = Field(..., ge=0.0)

    # FIX: Changed from `date` to `datetime` to handle timestamps like "2026-08-18T10:00:00"
    fee_paid_date: datetime

    pending_fee_amount: float = Field(default=0.0, ge=0.0)
    next_fee_date: Optional[date] = None
    is_fee_fully_paid: bool = False


@app.post("/create_student")
def student_create(student: CreateStudent):
    students_db = load_student_data()

    student_dict = json.loads(student.json())
    # Pydantic v2: mode='json' date/datetime objects ko string mein convert karta hai
    if students_db:
        # Get the max ID existing in the file and add 1
        new_id = max(s.get("id", 0) for s in students_db) + 1
    else:
          new_id = 1

    # Insert the generated ID at the start of the dictionary
    student_dict["id"] = new_id
        
    students_db.append(student_dict)
    save_student_data(students_db)
    return {"message": "Student created successfully", "student": student}

class adminCreate(BaseModel):
    firstName: str = Field(..., min_length=2, example="Rohit")
    lastName: str = Field(..., min_length=2, example="Kumar")
    phone: int = Field(..., max_length=10, example="Kumar")
    email: email

@app.post("/aadmin_Create")
def adminSignup(AdminSignUP: adminCreate):
    