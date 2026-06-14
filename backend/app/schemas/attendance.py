from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class AttendanceBase(BaseModel):
    student_id: UUID
    date: datetime
    status: str # present, absent, late, half-day
    remarks: Optional[str] = None

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    id: UUID
    school_id: UUID

    class Config:
        from_attributes = True

class BulkAttendanceCreate(BaseModel):
    records: List[AttendanceCreate]
