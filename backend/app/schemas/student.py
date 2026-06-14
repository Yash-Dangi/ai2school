from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    current_grade_id: Optional[UUID] = None

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: UUID
    school_id: UUID
    admission_number: str

    class Config:
        from_attributes = True
