from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str

class CourseCreate(CourseBase):
    student_id: int

class Course(CourseBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    courses: list[Course] = []

    class Config:
        orm_mode = True