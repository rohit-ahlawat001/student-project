from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

students_db = [
    {
        "id": 1, "name": "Riya Sharma", "course": "MCA", "semester": 3,
        "fee_paid_amount": 45000, "fee_paid_date": "2026-08-15T10:30:00", 
        "pending_fee_amount": 15000, "next_fee_date": "2026-10-15", 
        "is_fee_fully_paid": False
    },
    {
        "id": 2, "name": "Aman Verma", "course": "BCA", "semester": 5,
        "fee_paid_amount": 35000, "fee_paid_date": "2026-07-20T14:15:00", 
        "pending_fee_amount": 0, "next_fee_date": None, 
        "is_fee_fully_paid": True
    },
    {
        "id": 3, "name": "Priya Singh", "course": "MCA", "semester": 1,
        "fee_paid_amount": 30000, "fee_paid_date": "2026-08-25T09:45:00", 
        "pending_fee_amount": 30000, "next_fee_date": "2026-11-01", 
        "is_fee_fully_paid": False
    },
    {
        "id": 4, "name": "Karan Mehta", "course": "BTech", "semester": 4,
        "fee_paid_amount": 80000, "fee_paid_date": "2026-07-10T11:00:00", 
        "pending_fee_amount": 0, "next_fee_date": None, 
        "is_fee_fully_paid": True
    },
    {
        "id": 5, "name": "Neha Gupta", "course": "BCA", "semester": 2,
        "fee_paid_amount": 15000, "fee_paid_date": "2026-09-01T16:20:00", 
        "pending_fee_amount": 20000, "next_fee_date": "2026-10-05", 
        "is_fee_fully_paid": False
    },
    {
        "id": 6, "name": "Rahul Das", "course": "BTech", "semester": 6,
        "fee_paid_amount": 40000, "fee_paid_date": "2026-08-05T13:10:00", 
        "pending_fee_amount": 40000, "next_fee_date": "2026-12-10", 
        "is_fee_fully_paid": False
    },
    {
        "id": 7, "name": "Sneha Patel", "course": "MCA", "semester": 2,
        "fee_paid_amount": 60000, "fee_paid_date": "2026-07-28T10:05:00", 
        "pending_fee_amount": 0, "next_fee_date": None, 
        "is_fee_fully_paid": True
    },
    {
        "id": 8, "name": "Rohan Khanna", "course": "BTech", "semester": 8,
        "fee_paid_amount": 75000, "fee_paid_date": "2026-06-15T12:00:00", 
        "pending_fee_amount": 5000, "next_fee_date": "2026-09-15", 
        "is_fee_fully_paid": False
    },
    {
        "id": 9, "name": "Anjali Desai", "course": "BBA", "semester": 3,
        "fee_paid_amount": 45000, "fee_paid_date": "2026-08-10T15:40:00", 
        "pending_fee_amount": 0, "next_fee_date": None, 
        "is_fee_fully_paid": True
    },
    {
        "id": 10, "name": "Vikram Raj", "course": "BCA", "semester": 1,
        "fee_paid_amount": 10000, "fee_paid_date": "2026-09-02T09:15:00", 
        "pending_fee_amount": 25000, "next_fee_date": "2026-10-20", 
        "is_fee_fully_paid": False
    },
    {
        "id": 11, "name": "Pooja Joshi", "course": "MCA", "semester": 4,
        "fee_paid_amount": 50000, "fee_paid_date": "2026-07-05T14:30:00", 
        "pending_fee_amount": 10000, "next_fee_date": "2026-09-30", 
        "is_fee_fully_paid": False
    },
    {
        "id": 12, "name": "Aditya Nair", "course": "BTech", "semester": 2,
        "fee_paid_amount": 80000, "fee_paid_date": "2026-08-22T11:50:00", 
        "pending_fee_amount": 0, "next_fee_date": None, 
        "is_fee_fully_paid": True
    },
    {
        "id": 13, "name": "Kriti Sen", "course": "MBA", "semester": 1,
        "fee_paid_amount": 100000, "fee_paid_date": "2026-08-18T10:00:00", 
        "pending_fee_amount": 50000, "next_fee_date": "2026-11-15", 
        "is_fee_fully_paid": False
    },
    {
        "id": 14, "name": "Siddharth Rao", "course": "BBA", "semester": 5,
        "fee_paid_amount": 45000, "fee_paid_date": "2026-07-22T16:45:00", 
        "pending_fee_amount": 0, "next_fee_date": None, 
        "is_fee_fully_paid": True
    }
]

@app.get("/students_list")
def getStudents():
  result = students_db
  return result

@app.get("/student-view/{student_id}")
def viewStudent(student_id: int):
    for stu in students_db:
       if stu["id"] == student_id:
          return stu
    return {"message": 'kindly search for the valid student'}

#Ading the delete student Endpoint 