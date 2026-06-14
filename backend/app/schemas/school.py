from pydantic import BaseModel
from typing import Optional, Dict, List
from uuid import UUID

# Subject Schemas
class SubjectBase(BaseModel):
    name: Dict[str, str] # e.g. {"en": "Mathematics", "hi": "गणित"}
    code: str

class MasterSubject(BaseModel):
    code: str
    name_en: str

class SubjectCreate(BaseModel):
    master_code: str

class SubjectResponse(SubjectBase):
    id: UUID
    school_id: UUID

    class Config:
        from_attributes = True

# Grade Schemas
class GradeBase(BaseModel):
    name: Dict[str, str]
    level: int

class GradeCreate(GradeBase):
    pass

class GradeResponse(GradeBase):
    id: UUID
    school_id: UUID

    class Config:
        from_attributes = True
