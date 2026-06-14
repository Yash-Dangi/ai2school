from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class StaffBase(BaseModel):
    employee_id: str
    first_name: str
    last_name: str
    designation: Optional[str] = None

class StaffCreate(StaffBase):
    pass

class StaffResponse(StaffBase):
    id: UUID
    school_id: UUID

    class Config:
        from_attributes = True
