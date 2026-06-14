from typing import Any, List
import random
import string
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api import deps
from app.models.core import Student, User
from app.schemas.student import StudentCreate, StudentResponse

router = APIRouter()

def generate_admission_number() -> str:
    # MVP simple admission number generator: ADM-XXXXX
    rand_str = ''.join(random.choices(string.digits, k=5))
    return f"ADM-{rand_str}"

@router.get("/", response_model=List[StudentResponse])
async def read_students(
    db: AsyncSession = Depends(deps.get_db),
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Retrieve students for the school."""
    result = await db.execute(select(Student).filter(Student.school_id == school_id))
    return result.scalars().all()

@router.post("/", response_model=StudentResponse)
async def create_student(
    *,
    db: AsyncSession = Depends(deps.get_db),
    student_in: StudentCreate,
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Create new student."""
    if current_user.role not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
        
    admission_number = generate_admission_number()
    db_student = Student(
        **student_in.model_dump(), 
        school_id=school_id, 
        admission_number=admission_number
    )
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student
