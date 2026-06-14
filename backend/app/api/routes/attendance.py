from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime

from app.api import deps
from app.models.core import Attendance, User
from app.schemas.attendance import AttendanceCreate, AttendanceResponse, BulkAttendanceCreate

router = APIRouter()

@router.get("/", response_model=List[AttendanceResponse])
async def read_attendance(
    date_str: str = None,
    db: AsyncSession = Depends(deps.get_db),
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Retrieve attendance records."""
    query = select(Attendance).filter(Attendance.school_id == school_id)
    if date_str:
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            # In a real app we'd cast to date in the DB query, but for MVP we fetch all or filter strictly
            # query = query.filter(cast(Attendance.date, Date) == target_date)
        except ValueError:
            pass
    
    result = await db.execute(query)
    return result.scalars().all()

@router.post("/bulk", response_model=List[AttendanceResponse])
async def create_bulk_attendance(
    *,
    db: AsyncSession = Depends(deps.get_db),
    attendance_in: BulkAttendanceCreate,
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Bulk insert attendance records."""
    if current_user.role not in ["superadmin", "admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
        
    db_records = []
    for record in attendance_in.records:
        db_att = Attendance(**record.model_dump(), school_id=school_id)
        db.add(db_att)
        db_records.append(db_att)
        
    await db.commit()
    for record in db_records:
        await db.refresh(record)
        
    return db_records
