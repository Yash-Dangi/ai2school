import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, JSON, Integer, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from .base import Base

class School(Base):
    __tablename__ = "schools"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    code = Column(String(50), unique=True, index=True, nullable=False)
    board = Column(String(50), nullable=False)  # e.g., CBSE
    config = Column(JSONB, default=dict)        # Flexible config (i18n, preferences)
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = relationship("User", back_populates="school")
    students = relationship("Student", back_populates="school")
    staff = relationship("Staff", back_populates="school")
    grades = relationship("Grade", back_populates="school")
    subjects = relationship("Subject", back_populates="school")

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=True) # Null for SuperAdmin
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False) # superadmin, admin, teacher, parent, student
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    school = relationship("School", back_populates="users")

class Student(Base):
    __tablename__ = "students"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=False)
    admission_number = Column(String(50), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    
    current_grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id"))
    
    school = relationship("School", back_populates="students")
    grade = relationship("Grade")

class Staff(Base):
    __tablename__ = "staff"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=False)
    employee_id = Column(String(50), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    designation = Column(String(100))
    
    school = relationship("School", back_populates="staff")

class Grade(Base):
    """Represents Class 9, Class 10, etc."""
    __tablename__ = "grades"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=False)
    name = Column(JSONB, nullable=False) # e.g. {"en": "Class 9", "hi": "कक्षा ९"}
    level = Column(Integer, nullable=False) # 9, 10, 11, 12
    
    school = relationship("School", back_populates="grades")

class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=False)
    name = Column(JSONB, nullable=False) # e.g. {"en": "Mathematics", "hi": "गणित"}
    code = Column(String(50), nullable=False)
    
    school = relationship("School", back_populates="subjects")

class SubjectTeacher(Base):
    __tablename__ = "subject_teachers"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=False)
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"), nullable=False)
    staff_id = Column(UUID(as_uuid=True), ForeignKey("staff.id"), nullable=False)
    grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id"), nullable=False)
    
    subject = relationship("Subject")
    staff = relationship("Staff")
    grade = relationship("Grade")

class Attendance(Base):
    __tablename__ = "attendance"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String(20), nullable=False) # present, absent, late, half-day
    remarks = Column(Text, nullable=True)

    student = relationship("Student")

class Exam(Base):
    __tablename__ = "exams"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=False)
    name = Column(JSONB, nullable=False) # e.g. {"en": "Half Yearly", "hi": "अर्धवार्षिक"}
    grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id"), nullable=False)
    
    grade = relationship("Grade")

class ExamScore(Base):
    __tablename__ = "exam_scores"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"), nullable=False)
    exam_id = Column(UUID(as_uuid=True), ForeignKey("exams.id"), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"), nullable=False)
    
    marks_obtained = Column(Integer, nullable=False)
    max_marks = Column(Integer, nullable=False)
    
    exam = relationship("Exam")
    student = relationship("Student")
    subject = relationship("Subject")
