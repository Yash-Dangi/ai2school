from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import auth, school, staff, student, attendance, exam, report, ai

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For dev, restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(school.router, prefix=f"{settings.API_V1_STR}/school", tags=["school"])
app.include_router(staff.router, prefix=f"{settings.API_V1_STR}/staff", tags=["staff"])
app.include_router(student.router, prefix=f"{settings.API_V1_STR}/student", tags=["student"])
app.include_router(attendance.router, prefix=f"{settings.API_V1_STR}/attendance", tags=["attendance"])
app.include_router(exam.router, prefix=f"{settings.API_V1_STR}/exam", tags=["exam"])
app.include_router(report.router, prefix=f"{settings.API_V1_STR}/report", tags=["report"])
app.include_router(ai.router, prefix=f"{settings.API_V1_STR}/ai", tags=["ai"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
