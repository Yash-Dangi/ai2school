from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api import deps
from app.models.core import Student, Exam, ExamScore, Subject, Attendance, User

router = APIRouter()

@router.get("/{student_id}/report-card/{exam_id}")
async def generate_report_card(
    student_id: str,
    exam_id: str,
    lang: str = "en",
    db: AsyncSession = Depends(deps.get_db),
    school_id: str = Depends(deps.get_school_id),
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """Generate a bilingual report card for a student."""
    
    # 1. Get Student
    student = await db.get(Student, student_id)
    if not student or str(student.school_id) != school_id:
        raise HTTPException(status_code=404, detail="Student not found")
        
    # 2. Get Exam
    exam = await db.get(Exam, exam_id)
    if not exam or str(exam.school_id) != school_id:
        raise HTTPException(status_code=404, detail="Exam not found")
        
    # 3. Get Scores with Subjects
    scores_result = await db.execute(
        select(ExamScore, Subject)
        .join(Subject, ExamScore.subject_id == Subject.id)
        .filter(ExamScore.student_id == student_id, ExamScore.exam_id == exam_id)
    )
    scores_data = scores_result.all()
    
    # 4. Get Attendance Stats (simplified for MVP)
    att_result = await db.execute(select(Attendance).filter(Attendance.student_id == student_id))
    attendances = att_result.scalars().all()
    total_days = len(attendances)
    present_days = sum(1 for a in attendances if a.status == "present")
    
    # 5. Format Output dynamically based on JSONB
    # Support fallback to English if the requested language translation doesn't exist
    
    report_card = {
        "student_name": f"{student.first_name} {student.last_name}",
        "admission_number": student.admission_number,
        "exam_name": exam.name.get(lang, exam.name.get("en", "Unknown Exam")),
        "attendance": {
            "total_days": total_days,
            "present_days": present_days,
            "percentage": round((present_days / total_days * 100), 2) if total_days > 0 else 0
        },
        "scores": []
    }
    
    total_obtained = 0
    total_max = 0
    
    for score, subject in scores_data:
        subj_name = subject.name.get(lang, subject.name.get("en", "Unknown Subject"))
        report_card["scores"].append({
            "subject": subj_name,
            "marks_obtained": score.marks_obtained,
            "max_marks": score.max_marks
        })
        total_obtained += score.marks_obtained
        total_max += score.max_marks
        
    report_card["total"] = {
        "obtained": total_obtained,
        "max": total_max,
        "percentage": round((total_obtained / total_max * 100), 2) if total_max > 0 else 0
    }
    
    return report_card
