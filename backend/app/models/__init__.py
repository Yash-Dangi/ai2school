from .base import Base
from .core import School, User, Student, Staff, Grade, Subject

# For Alembic to discover all models
__all__ = ["Base", "School", "User", "Student", "Staff", "Grade", "Subject"]
