# Module 5: AI Analytics — Complete Design

---

## Overview

AI Analytics transforms raw school data into actionable insights for every stakeholder. Unlike static reports, these dashboards use AI to surface patterns, predict outcomes, and recommend interventions.

---

## 5.1 Student Analytics Dashboard

### Audience: Teachers, Academic Heads, Parents (filtered view)

### Metrics & Visualizations

#### Individual Student View

| Metric | Visualization | Data Source | AI Enhancement |
|---|---|---|---|
| **Overall Performance Trend** | Line chart (term-wise) | Exam marks | Trend prediction: "Likely to score X in finals" |
| **Subject-wise Performance** | Radar chart | Exam marks | Strength/weakness identification |
| **Chapter Mastery** | Heatmap (chapters × mastery level) | Quiz, practice, exams | Learning gap detection |
| **Attendance Correlation** | Scatter plot (attendance % vs. marks) | Attendance + Exams | "Attendance dropped in May → marks declined in June" |
| **Homework Completion Rate** | Progress bar by subject | LMS | Consistency tracking |
| **AI Tutor Usage** | Usage stats (sessions, topics, time) | Tutor sessions | "Most doubts in Algebra — needs focused practice" |
| **Improvement Areas** | Prioritized list | All data | AI-generated recommendations |

#### AI-Generated Insights (per student)

```json
{
  "student_id": "...",
  "insights": [
    {
      "type": "learning_gap",
      "severity": "high",
      "message": "Struggling with 'Quadratic Equations' — scored below 40% in last 3 assessments",
      "recommendation": "Focus 30 minutes daily on Chapter 4 practice. AI Practice Mode recommended.",
      "data_points": ["unit_test_2: 35%", "quiz_avg: 38%", "homework_completion: 50%"]
    },
    {
      "type": "improvement",
      "severity": "positive",
      "message": "Significant improvement in Science — up 15% from last term",
      "recommendation": "Continue current study pattern. Ready for advanced questions.",
      "data_points": ["term1: 62%", "term2: 77%"]
    },
    {
      "type": "attendance_alert",
      "severity": "medium",
      "message": "Attendance dropped to 78% in the last month (was 95% earlier)",
      "recommendation": "Check with parents. Possible correlation with declining Math scores.",
      "data_points": ["last_30_days: 78%", "previous_average: 95%"]
    },
    {
      "type": "at_risk",
      "severity": "high",
      "message": "At-risk of failing Mathematics if current trajectory continues",
      "recommendation": "Schedule parent meeting. Consider remedial classes.",
      "prediction_confidence": 0.82
    }
  ],
  "summary": "Arjun is performing well in Science and English but needs significant support in Mathematics, particularly in Algebra and Geometry. Attendance has declined recently which may be contributing to the academic dip."
}
```

#### At-Risk Student Detection Algorithm

```
function calculateRiskScore(student):
    risk_factors = {
        "declining_grades": checkGradeTrend(student, last_3_exams),        // 0-25 points
        "low_attendance": (100 - attendance_percentage) * 0.3,              // 0-30 points
        "homework_gaps": (100 - homework_completion_rate) * 0.2,            // 0-20 points
        "failing_subjects": count_failing_subjects * 5,                      // 0-25 points
        "attendance_decline": checkAttendanceTrend(student) * 10,           // 0-10 points
        "engagement_drop": checkEngagementTrend(student) * 0.1              // 0-10 points
    }
    
    total_risk = sum(risk_factors.values())
    
    if total_risk > 60: return "HIGH_RISK"
    if total_risk > 35: return "MEDIUM_RISK"
    if total_risk > 15: return "LOW_RISK"
    return "ON_TRACK"
```

---

## 5.2 Teacher Analytics Dashboard

### Audience: Teachers (own classes), Coordinators (department), Academic Heads (all)

### Metrics & Visualizations

| Metric | Visualization | Purpose |
|---|---|---|
| **Class Performance Distribution** | Bell curve / Box plot | See spread: how many students are excelling vs. struggling |
| **Subject Average Comparison** | Bar chart (sections side-by-side) | Compare performance across sections |
| **Chapter-wise Performance** | Stacked bar (chapter × difficulty) | Identify which chapters students found hard |
| **Assessment Insights** | Question-level analysis | Which questions had lowest accuracy → teaching gap |
| **Question Quality Analysis** | Difficulty vs. discrimination index | AI evaluates if test questions were effective |
| **Homework Completion Trends** | Line chart over time | Track engagement |
| **Curriculum Coverage** | Gantt chart (planned vs. actual) | Track syllabus completion |
| **Student Attention Alerts** | Priority list | AI-flagged students needing intervention |

#### AI-Generated Teaching Insights

```json
{
  "teacher_id": "...",
  "class": "8-A",
  "subject": "Mathematics",
  "insights": [
    {
      "type": "teaching_gap",
      "message": "75% of students scored below 50% on 'Rational Numbers' questions in Unit Test 2",
      "recommendation": "Consider revisiting Chapter 1 with more worked examples. AI Worksheet (Practice) available for students.",
      "affected_students": 30
    },
    {
      "type": "assessment_quality",
      "message": "Q7 in Unit Test 2 had 95% accuracy — it may have been too easy for the allocated 5 marks",
      "recommendation": "Consider increasing difficulty of long-answer questions to better discriminate student understanding"
    },
    {
      "type": "cross_section_comparison",
      "message": "Section A averages 72% while Section B averages 58% in the same subject",
      "recommendation": "Review teaching approach differences. Consider sharing effective strategies with Section B teacher."
    }
  ]
}
```

---

## 5.3 Principal Analytics Dashboard

### Audience: Principal, Vice Principal, Directors

### Dashboard Layout

```
┌─────────────────────────────────────────────────────────────┐
│                    SCHOOL HEALTH SCORE                       │
│                      ████████░░ 82/100                      │
│  Academic: 85  │  Attendance: 88  │  Operations: 78  │ AI: 75│
├─────────────────────────────────────────────────────────────┤
│ TODAY'S SNAPSHOT                                             │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│ │Students  │ │Teachers  │ │Attendance│ │Fee        │       │
│ │Present   │ │Present   │ │Rate      │ │Collection │       │
│ │ 1,247    │ │  78/82   │ │  94.2%   │ │ ₹12.4L   │       │
│ │ /1,320   │ │          │ │          │ │ today     │       │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
├─────────────────────────────────────────────────────────────┤
│ AI ALERTS (Priority)                                        │
│ 🔴 15 students at HIGH risk of failing Math (Class 10)     │
│ 🟡 Attendance below 75% for 23 students (attendance notice)│
│ 🟢 Science results improved 12% over last term             │
│ 🔵 3 teachers have >5 pending leave requests               │
├─────────────────┬───────────────────────────────────────────┤
│ ACADEMIC        │ DEPARTMENT PERFORMANCE                    │
│ PERFORMANCE     │ ┌─────────────────────────────┐           │
│ Term-wise trend │ │ Science    ████████░░ 82%   │           │
│ [Line Chart]    │ │ Math       ██████░░░░ 68%   │           │
│                 │ │ English    ████████░░ 79%   │           │
│                 │ │ Social Sci ███████░░░ 75%   │           │
│                 │ │ Hindi      ████████░░ 81%   │           │
│                 │ └─────────────────────────────┘           │
├─────────────────┴───────────────────────────────────────────┤
│ ATTENDANCE TRENDS          │ FEE COLLECTION STATUS          │
│ [Heatmap: Days × Classes]  │ [Pie: Collected/Pending/      │
│                             │  Overdue]                      │
│                             │ Total Due: ₹1.2 Cr            │
│                             │ Collected: ₹98L (82%)         │
│                             │ Overdue: ₹22L (18%)           │
└─────────────────────────────────────────────────────────────┘
```

### Metrics

| Category | Metric | Computation |
|---|---|---|
| **Academic** | School Average Score | Weighted average across all exams |
| **Academic** | Pass Rate | Students scoring above passing marks / Total |
| **Academic** | Grade Distribution | Count per grade bucket (A+, A, B+, ...) |
| **Academic** | Subject Performance Ranking | Average by subject, ranked |
| **Academic** | Year-over-Year Improvement | Current vs. previous year same exam |
| **Academic** | Board Exam Prediction (Class 10, 12) | AI prediction based on internal exams |
| **Attendance** | Daily Attendance Rate | Present / Total (school-wide) |
| **Attendance** | Chronic Absentees | Students with <75% attendance |
| **Attendance** | Attendance Trends | Week-over-week, month-over-month |
| **Attendance** | Teacher Attendance | Staff present / total |
| **Financial** | Fee Collection Rate | Collected / Total Due |
| **Financial** | Overdue Amount | Sum of past-due invoices |
| **Financial** | Collection Trend | Daily/weekly collection amounts |
| **Operations** | Timetable Coverage | Classes with assigned timetables |
| **Operations** | Curriculum Completion | % of syllabus completed vs. planned |
| **AI Adoption** | AI Copilot Usage | Teachers using AI tools (%) |
| **AI Adoption** | AI Tutor Engagement | Students using AI tutor (%) |

### AI-Powered Insights for Principal

1. **Predictive Alerts**: "Based on mid-term results, 15 Class 10 students are at risk of failing board exams. Recommend remedial action."
2. **Teacher Effectiveness**: "Mr. Verma's Physics classes consistently outperform school average by 12%. Consider peer mentoring program."
3. **Trend Detection**: "Hindi performance has been declining across Classes 6-8 for 3 consecutive terms. Investigate."
4. **Operational Insights**: "Fee collection is 18% behind target. 45% of overdue is from Classes 3-5. Recommend targeted follow-up."
5. **Benchmarking** (multi-school): "Campus B is outperforming Campus A in Science by 15%. Teaching methodology difference identified."

---

## 5.4 Parent Analytics Dashboard

### Audience: Parents (per-child view only)

### Dashboard Content

```
┌─────────────────────────────────────────────────────────────┐
│ 👧 Ananya Sharma  │  Class 7-A  │  Roll No. 15            │
├─────────────────────────────────────────────────────────────┤
│ OVERALL PROGRESS                                            │
│ ┌───────────────────────────────────────────────┐           │
│ │ Class Rank: 8/40  │  Attendance: 94%  │ HW: 88% │       │
│ └───────────────────────────────────────────────┘           │
├─────────────────────────────────────────────────────────────┤
│ SUBJECT-WISE PERFORMANCE          │ AI RECOMMENDATIONS      │
│                                    │                         │
│ [Radar Chart]                      │ 📚 Ananya should       │
│   Math: 82%                        │    practice Algebra     │
│   Science: 91%                     │    20 min/day          │
│   English: 78%                     │                         │
│   Hindi: 72%                       │ 🎯 Strong in Science   │
│   SST: 85%                         │    — encourage for      │
│                                    │    Science Olympiad     │
│                                    │                         │
│                                    │ ⏰ Study plan available │
│                                    │    for upcoming exams   │
├─────────────────────────────────────────────────────────────┤
│ RECENT ACTIVITY                                             │
│ ● Jun 12: Scored 85/100 in Science Unit Test 3             │
│ ● Jun 11: Submitted Math Homework (on time)                │
│ ● Jun 10: Attended AI Tutor session — Algebra (25 min)     │
│ ● Jun 9: Absent (Excused — Sick leave approved)            │
├─────────────────────────────────────────────────────────────┤
│ TERM COMPARISON                                             │
│ [Bar chart: Term 1 vs Term 2 per subject]                  │
│ 📈 Improved in: Science (+8%), SST (+5%)                   │
│ 📉 Needs attention: Hindi (-3%)                            │
└─────────────────────────────────────────────────────────────┘
```

### AI-Generated Parent Summary (Weekly)

Delivered via WhatsApp / Push notification / Email:

```
📊 Weekly Progress Summary for Ananya (Class 7-A)
Week of June 8-14, 2025

✅ Attendance: 5/5 days (100%)
📝 Homework: 4/5 submitted on time
🏆 Best Performance: Science Unit Test — 85/100 (Class rank: 5th)
📚 AI Tutor: Used 3 times this week (Algebra, Fractions)

💡 AI Recommendation:
Ananya is doing well in Science! She would benefit from 
extra practice in Hindi grammar — suggest 15 min daily reading.

📅 Upcoming: Math Unit Test on June 18
```

---

## Analytics Database Tables

```sql
-- Pre-computed Analytics (refreshed periodically)
CREATE TABLE analytics_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    school_id UUID NOT NULL REFERENCES schools(id),
    academic_year_id UUID NOT NULL REFERENCES academic_years(id),
    
    scope_type VARCHAR(20) NOT NULL, -- school, grade, section, student, teacher
    scope_id UUID, -- ID of the scoped entity
    
    metric_name VARCHAR(100) NOT NULL,
    metric_value DECIMAL(10,2),
    metric_data JSONB, -- Complex metric data
    
    period_type VARCHAR(20), -- daily, weekly, monthly, term, yearly
    period_start DATE,
    period_end DATE,
    
    computed_at TIMESTAMP DEFAULT NOW(),
    
    UNIQUE(school_id, academic_year_id, scope_type, scope_id, metric_name, period_type, period_start)
);

CREATE INDEX idx_analytics_scope ON analytics_snapshots(school_id, scope_type, scope_id, metric_name);

-- AI-Generated Insights
CREATE TABLE ai_insights (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    school_id UUID NOT NULL REFERENCES schools(id),
    
    target_type VARCHAR(20) NOT NULL, -- student, teacher, class, school
    target_id UUID NOT NULL,
    
    insight_type VARCHAR(30) NOT NULL, 
    -- learning_gap, improvement, at_risk, attendance_alert, 
    -- teaching_gap, achievement, recommendation, prediction
    
    severity VARCHAR(10) NOT NULL, -- positive, low, medium, high, critical
    title VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    recommendation TEXT,
    data_points JSONB,
    confidence_score DECIMAL(3,2), -- 0-1
    
    -- Status
    status VARCHAR(20) DEFAULT 'active', -- active, acknowledged, acted_upon, dismissed
    acknowledged_by UUID REFERENCES users(id),
    acknowledged_at TIMESTAMP,
    action_taken TEXT,
    
    -- Visibility
    visible_to_roles TEXT[], -- ['teacher', 'principal', 'parent']
    
    generated_at TIMESTAMP DEFAULT NOW(),
    expires_at TIMESTAMP,
    
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_ai_insights_target ON ai_insights(school_id, target_type, target_id, status);

-- Student Risk Scores
CREATE TABLE student_risk_scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL REFERENCES students(id),
    school_id UUID NOT NULL REFERENCES schools(id),
    academic_year_id UUID NOT NULL REFERENCES academic_years(id),
    
    overall_risk_score DECIMAL(5,2) NOT NULL, -- 0-100
    risk_level VARCHAR(20) NOT NULL, -- on_track, low_risk, medium_risk, high_risk
    
    risk_factors JSONB NOT NULL,
    -- {
    --   "declining_grades": {"score": 15, "details": "..."},
    --   "low_attendance": {"score": 20, "details": "..."},
    --   "homework_gaps": {"score": 10, "details": "..."},
    --   ...
    -- }
    
    trending VARCHAR(10), -- improving, stable, declining
    
    computed_at TIMESTAMP DEFAULT NOW(),
    
    UNIQUE(student_id, academic_year_id)
);
```

### Analytics API Endpoints

```
# Student Analytics
GET    /api/v1/analytics/students/{studentId}/overview       # Student overview
GET    /api/v1/analytics/students/{studentId}/performance     # Performance trends
GET    /api/v1/analytics/students/{studentId}/insights        # AI insights
GET    /api/v1/analytics/students/{studentId}/risk            # Risk assessment

# Class Analytics
GET    /api/v1/analytics/classes/{classId}/performance        # Class performance
GET    /api/v1/analytics/classes/{classId}/comparison         # Section comparison
GET    /api/v1/analytics/classes/{classId}/at-risk            # At-risk students list

# Teacher Analytics
GET    /api/v1/analytics/teachers/{teacherId}/dashboard       # Teacher dashboard
GET    /api/v1/analytics/teachers/{teacherId}/insights        # Teaching insights

# School Analytics
GET    /api/v1/analytics/school/dashboard                     # Principal dashboard
GET    /api/v1/analytics/school/academic                      # Academic metrics
GET    /api/v1/analytics/school/attendance                     # Attendance analytics
GET    /api/v1/analytics/school/financial                      # Fee analytics
GET    /api/v1/analytics/school/ai-adoption                    # AI usage metrics

# Parent Analytics
GET    /api/v1/analytics/parent/{studentId}/summary            # Child's summary
GET    /api/v1/analytics/parent/{studentId}/weekly-report       # Weekly AI report

# Multi-School Analytics
GET    /api/v1/analytics/group/comparison                      # Cross-campus comparison
GET    /api/v1/analytics/group/benchmarks                      # Benchmarking

# Insights Management
GET    /api/v1/analytics/insights                              # List insights (filtered)
PUT    /api/v1/analytics/insights/{id}/acknowledge             # Acknowledge insight
PUT    /api/v1/analytics/insights/{id}/action                  # Record action taken
```

---

*Next: [Module 6: Parent Portal →](./07-module-parent-portal.md)*
