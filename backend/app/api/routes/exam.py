from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api import deps
from app.models.core import Exam, ExamScore, User
from app.schemas.exam import ExamCreate, ExamResponse, BulkExamScoreCreate, ExamScoreResponse

router = APIRouter()

@router.get("/", response_model=List[ExamResponse])
async def read_exams(
    db: AsyncSession = Depends(deps.get_db),
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Retrieve exams for the school."""
    result = await db.execute(select(Exam).filter(Exam.school_id == school_id))
    return result.scalars().all()

@router.post("/", response_model=ExamResponse)
async def create_exam(
    *,
    db: AsyncSession = Depends(deps.get_db),
    exam_in: ExamCreate,
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Create new exam."""
    if current_user.role not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
        
    db_exam = Exam(**exam_in.model_dump(), school_id=school_id)
    db.add(db_exam)
    await db.commit()
    await db.refresh(db_exam)
    return db_exam

@router.get("/{exam_id}/scores", response_model=List[ExamScoreResponse])
async def read_exam_scores(
    exam_id: str,
    db: AsyncSession = Depends(deps.get_db),
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Retrieve scores for a specific exam."""
    result = await db.execute(
        select(ExamScore).filter(
            ExamScore.school_id == school_id,
            ExamScore.exam_id == exam_id
        )
    )
    return result.scalars().all()

@router.post("/scores/bulk", response_model=List[ExamScoreResponse])
async def create_bulk_scores(
    *,
    db: AsyncSession = Depends(deps.get_db),
    scores_in: BulkExamScoreCreate,
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Bulk insert exam scores."""
    if current_user.role not in ["superadmin", "admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
        
    db_records = []
    for score in scores_in.scores:
        db_score = ExamScore(**score.model_dump(), exam_id=scores_in.exam_id, school_id=school_id)
        db.add(db_score)
        db_records.append(db_score)
        
    await db.commit()
    for record in db_records:
        await db.refresh(record)
        
    return db_records
