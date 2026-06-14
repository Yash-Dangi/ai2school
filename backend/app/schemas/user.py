from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    role: str

class UserCreate(UserBase):
    password: str
    school_id: Optional[UUID] = None

class UserResponse(UserBase):
    id: UUID
    school_id: Optional[UUID]
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
