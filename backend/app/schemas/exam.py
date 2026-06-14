from pydantic import BaseModel
from typing import Optional, Dict, List
from uuid import UUID

class ExamBase(BaseModel):
    name: Dict[str, str] # e.g. {"en": "Half Yearly", "hi": "अर्धवार्षिक"}
    grade_id: UUID

class ExamCreate(ExamBase):
    pass

class ExamResponse(ExamBase):
    id: UUID
    school_id: UUID

    class Config:
        from_attributes = True

class ExamScoreBase(BaseModel):
    student_id: UUID
    subject_id: UUID
    marks_obtained: int
    max_marks: int

class ExamScoreCreate(ExamScoreBase):
    pass

class ExamScoreResponse(ExamScoreBase):
    id: UUID
    school_id: UUID
    exam_id: UUID

    class Config:
        from_attributes = True

class BulkExamScoreCreate(BaseModel):
    exam_id: UUID
    scores: List[ExamScoreCreate]
