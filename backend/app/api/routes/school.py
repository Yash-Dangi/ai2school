from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api import deps
from app.models.core import Subject, Grade, User
from app.schemas.school import SubjectCreate, SubjectResponse, GradeCreate, GradeResponse, MasterSubject

router = APIRouter()

MASTER_SUBJECTS = {
    "MATH": {"en": "Mathematics", "hi": "गणित"},
    "SCI": {"en": "Science", "hi": "विज्ञान"},
    "SST": {"en": "Social Science", "hi": "सामाजिक विज्ञान"},
    "ENG": {"en": "English", "hi": "अंग्रेज़ी"},
    "HIN": {"en": "Hindi", "hi": "हिन्दी"},
    "PHY": {"en": "Physics", "hi": "भौतिक विज्ञान"},
    "CHEM": {"en": "Chemistry", "hi": "रसायन विज्ञान"},
    "BIO": {"en": "Biology", "hi": "जीव विज्ञान"},
    "CS": {"en": "Computer Science", "hi": "कंप्यूटर विज्ञान"},
    "ACC": {"en": "Accountancy", "hi": "लेखाशास्त्र"},
    "BST": {"en": "Business Studies", "hi": "व्यवसाय अध्ययन"},
    "ECO": {"en": "Economics", "hi": "अर्थशास्त्र"}
}

@router.get("/master-subjects", response_model=List[MasterSubject])
async def read_master_subjects(
    current_user: User = Depends(deps.get_current_active_user)
) -> Any:
    """Get list of standard subjects available to add."""
    return [{"code": code, "name_en": data["en"]} for code, data in MASTER_SUBJECTS.items()]

@router.get("/subjects", response_model=List[SubjectResponse])
async def read_subjects(
    db: AsyncSession = Depends(deps.get_db),
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Retrieve subjects for the school."""
    result = await db.execute(select(Subject).filter(Subject.school_id == school_id))
    return result.scalars().all()

@router.post("/subjects", response_model=SubjectResponse)
async def create_subject(
    *,
    db: AsyncSession = Depends(deps.get_db),
    subject_in: SubjectCreate,
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Create new subject from master catalog."""
    if current_user.role not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
        
    master_data = MASTER_SUBJECTS.get(subject_in.master_code)
    if not master_data:
        raise HTTPException(status_code=400, detail="Invalid master subject code")

    # Check if school already added this subject
    existing = await db.execute(select(Subject).filter(
        Subject.school_id == school_id, 
        Subject.code == subject_in.master_code
    ))
    if existing.scalars().first():
        raise HTTPException(status_code=400, detail="Subject already added to school")
        
    db_subject = Subject(
        code=subject_in.master_code,
        name=master_data,
        school_id=school_id
    )
    db.add(db_subject)
    await db.commit()
    await db.refresh(db_subject)
    return db_subject

@router.get("/grades", response_model=List[GradeResponse])
async def read_grades(
    db: AsyncSession = Depends(deps.get_db),
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Retrieve grades for the school."""
    result = await db.execute(select(Grade).filter(Grade.school_id == school_id))
    return result.scalars().all()

@router.post("/grades", response_model=GradeResponse)
async def create_grade(
    *,
    db: AsyncSession = Depends(deps.get_db),
    grade_in: GradeCreate,
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Create new grade."""
    if current_user.role not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
        
    db_grade = Grade(**grade_in.model_dump(), school_id=school_id)
    db.add(db_grade)
    await db.commit()
    await db.refresh(db_grade)
    return db_grade
