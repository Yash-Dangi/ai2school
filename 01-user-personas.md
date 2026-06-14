# AI2School — User Personas

---

## Persona 1: Student (Classes 1-12)

### Sub-Persona 1A: Primary Student (Classes 1-5)

| Attribute | Detail |
|---|---|
| **Name** | Ananya, Class 4 |
| **Age** | 9 years |
| **Tech Comfort** | Uses tablet at home, comfortable with touch interfaces |
| **Goals** | Complete homework on time, understand difficult math concepts, earn badges |
| **Frustrations** | Gets stuck on problems with no one to ask at home, boring worksheets |
| **Platform Usage** | AI Tutor (guided mode), Homework submission, Practice quizzes |
| **Interaction Model** | Visual, gamified, parent-supervised |

### Sub-Persona 1B: Middle School Student (Classes 6-8)

| Attribute | Detail |
|---|---|
| **Name** | Rohan, Class 7 |
| **Age** | 12 years |
| **Tech Comfort** | Uses phone and laptop, active on YouTube |
| **Goals** | Understand Science experiments, prepare for exams, track own progress |
| **Frustrations** | Too many subjects, inconsistent study habits, fear of exams |
| **Platform Usage** | AI Tutor, AI Doubt Solver, Study Planner, Quiz Generator |
| **Interaction Model** | Semi-independent, chat-based AI interaction |

### Sub-Persona 1C: Senior Student (Classes 9-12)

| Attribute | Detail |
|---|---|
| **Name** | Priya, Class 11 (Science) |
| **Age** | 16 years |
| **Tech Comfort** | Power user, uses multiple apps for study |
| **Goals** | Score 95%+ in boards, prepare for competitive exams, understand concepts deeply |
| **Frustrations** | Generic study material, no personalized revision, can't ask doubts at 11 PM |
| **Platform Usage** | AI Tutor (advanced), Exam Prep, Revision Assistant, Practice Mode |
| **Interaction Model** | Independent, detailed explanations, Bloom's higher-order questions |

---

## Persona 2: Teacher

### Sub-Persona 2A: Class Teacher

| Attribute | Detail |
|---|---|
| **Name** | Mrs. Sharma, Class 5 Teacher + English Teacher |
| **Age** | 35 years |
| **Tech Comfort** | Moderate, uses WhatsApp, basic computer skills |
| **Goals** | Finish syllabus on time, identify struggling students, communicate with parents |
| **Frustrations** | Spends weekends writing report card comments, manual attendance, repetitive lesson planning |
| **Platform Usage** | Attendance, AI Lesson Planner, AI Report Card Assistant, Parent Communication |
| **Key Metric** | Hours saved per week on administrative tasks |

### Sub-Persona 2B: Subject Teacher (Senior)

| Attribute | Detail |
|---|---|
| **Name** | Mr. Verma, Physics Teacher (Classes 11-12) |
| **Age** | 42 years |
| **Tech Comfort** | Good, uses technology for demonstrations |
| **Goals** | Create challenging question papers, track chapter-wise performance, differentiate instruction |
| **Frustrations** | Creating balanced question papers takes hours, no way to quickly identify weak students per topic |
| **Platform Usage** | AI Test Generator, AI Worksheet Generator, Analytics Dashboard, LMS |
| **Key Metric** | Question paper generation time, student performance improvement |

---

## Persona 3: Subject Coordinator

| Attribute | Detail |
|---|---|
| **Name** | Ms. Gupta, Mathematics Coordinator |
| **Age** | 40 years |
| **Tech Comfort** | Good |
| **Goals** | Ensure curriculum consistency across sections, mentor junior teachers, review assessment quality |
| **Frustrations** | No visibility into what different section teachers are doing, inconsistent question paper quality |
| **Platform Usage** | Curriculum mapping, cross-section analytics, lesson plan review, question bank management |
| **Key Metric** | Curriculum coverage consistency, assessment quality scores |

---

## Persona 4: Academic Head

| Attribute | Detail |
|---|---|
| **Name** | Dr. Mehta, Vice Principal (Academics) |
| **Age** | 50 years |
| **Tech Comfort** | Moderate |
| **Goals** | Improve board exam results, ensure CBSE compliance, monitor teaching quality |
| **Frustrations** | Gets data too late, reliant on teachers' self-reporting, no early warning for underperformance |
| **Platform Usage** | AI Analytics Dashboard, Exam Result Analytics, Teacher Performance, Curriculum Coverage |
| **Key Metric** | Board exam pass rate, average scores, teacher effectiveness ratings |

---

## Persona 5: School Administrator

| Attribute | Detail |
|---|---|
| **Name** | Mr. Khan, School Administrator |
| **Age** | 38 years |
| **Tech Comfort** | Good, primary ERP user |
| **Goals** | Collect fees on time, manage admissions efficiently, maintain records for compliance |
| **Frustrations** | Manual fee tracking, incomplete student records, audit preparation is chaos |
| **Platform Usage** | Admissions, Fee Management, Student Records, Staff Management, Reports |
| **Key Metric** | Fee collection rate, admission conversion, time-to-generate reports |

---

## Persona 6: Principal

| Attribute | Detail |
|---|---|
| **Name** | Mrs. Reddy, Principal |
| **Age** | 52 years |
| **Tech Comfort** | Basic to moderate |
| **Goals** | School reputation, student outcomes, parent satisfaction, operational efficiency |
| **Frustrations** | No single dashboard for school health, relies on verbal reports, surprised by problems |
| **Platform Usage** | Executive Dashboard, AI Analytics, Attendance Trends, Parent Feedback, Staff Overview |
| **Key Metric** | School health score, parent NPS, academic performance trends |

---

## Persona 7: Parent

### Sub-Persona 7A: Engaged Parent

| Attribute | Detail |
|---|---|
| **Name** | Mrs. Iyer, Mother of Class 6 student |
| **Age** | 38 years |
| **Tech Comfort** | High, smartphone power user |
| **Goals** | Track child's daily progress, ensure homework completion, communicate with teachers |
| **Frustrations** | Diary-based communication is unreliable, doesn't know what child is learning, fee payment is manual |
| **Platform Usage** | Parent App — Attendance, Homework, Grades, Fee Payment, AI Assistant |
| **Key Metric** | App engagement rate, satisfaction score |

### Sub-Persona 7B: Busy Parent

| Attribute | Detail |
|---|---|
| **Name** | Mr. Patel, Father of Class 3 student |
| **Age** | 42 years |
| **Tech Comfort** | Moderate, primarily WhatsApp |
| **Goals** | Get weekly summary of child's performance, pay fees online, attend PTMs |
| **Frustrations** | Too many messages from school, doesn't know what's important, misses deadlines |
| **Platform Usage** | WhatsApp notifications, weekly AI summary, fee payment |
| **Key Metric** | Message read rate, fee payment timeliness |

---

## Persona 8: Multi-School Management

| Attribute | Detail |
|---|---|
| **Name** | Mr. Agarwal, Director of Education (School Chain) |
| **Age** | 48 years |
| **Tech Comfort** | Good |
| **Goals** | Standardize across campuses, benchmark performance, optimize costs |
| **Frustrations** | Each school runs differently, no unified data, can't compare campuses |
| **Platform Usage** | Multi-school Dashboard, Benchmarking Analytics, Standardization Tools |
| **Key Metric** | Cross-campus consistency score, operational cost per student |

---

## Permission Matrix (RBAC Overview)

| Feature | Student | Teacher | Coordinator | Academic Head | Admin | Principal | Parent | Multi-School |
|---|---|---|---|---|---|---|---|---|
| Own Profile | View | View/Edit | View/Edit | View/Edit | View/Edit | View/Edit | View | View |
| Student Profiles | Own Only | Class Students | Department | All | All | All | Own Child | All Schools |
| Attendance (Mark) | ✗ | Own Classes | ✗ | ✗ | Bulk Edit | View All | ✗ | ✗ |
| Attendance (View) | Own | Own Classes | Department | All | All | All | Own Child | All Schools |
| Fee Management | View Own | ✗ | ✗ | ✗ | Full Access | View/Approve | View/Pay Own | All Schools |
| Exam Marks Entry | ✗ | Own Subjects | Review | Approve | ✗ | View/Approve | ✗ | View |
| AI Lesson Planner | ✗ | Full Access | Review/Edit | View | ✗ | View | ✗ | View |
| AI Test Generator | ✗ | Full Access | Review/Approve | View | ✗ | View | ✗ | View |
| AI Student Tutor | Full Access | ✗ | ✗ | ✗ | ✗ | ✗ | View Child's | ✗ |
| Analytics | Own Progress | Class Level | Department | School | Operations | School | Child | Multi-School |
| LMS Content | View/Submit | Create/Manage | Review | View | ✗ | View | View | View |
| Communication | Receive | Send to Parents | Send to Dept | Broadcast | Broadcast | Broadcast | Send to Teacher | Broadcast All |
| Staff Management | ✗ | ✗ | ✗ | View Dept | Full Access | Full Access | ✗ | All Schools |
| Timetable | View Own | View Own | View Dept | Edit | Edit | Approve | View Child | View All |
| Report Cards | View Own | Generate/Edit | Review | Approve | Print | Approve | View Child | View All |

---

*Next: [Module 1: School ERP →](./02-module-erp.md)*
