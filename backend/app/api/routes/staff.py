from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api import deps
from app.models.core import Staff, User
from app.schemas.staff import StaffCreate, StaffResponse

router = APIRouter()

@router.get("/", response_model=List[StaffResponse])
async def read_staff(
    db: AsyncSession = Depends(deps.get_db),
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Retrieve staff for the school."""
    result = await db.execute(select(Staff).filter(Staff.school_id == school_id))
    return result.scalars().all()

@router.post("/", response_model=StaffResponse)
async def create_staff(
    *,
    db: AsyncSession = Depends(deps.get_db),
    staff_in: StaffCreate,
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Create new staff member."""
    if current_user.role not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
        
    db_staff = Staff(**staff_in.model_dump(), school_id=school_id)
    db.add(db_staff)
    await db.commit()
    await db.refresh(db_staff)
    return db_staff
