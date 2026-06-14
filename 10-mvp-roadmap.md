# MVP Roadmap, Development Estimates, Risks & Non-Functional Requirements

---

## 1. MVP Roadmap

### Phase 1: Foundation (Months 1-3) — Must-Have

> **Goal**: Launch a usable School ERP + AI Copilot that can replace a school's existing system

#### Month 1: Core Infrastructure + Student Management

| Week | Deliverables |
|---|---|
| **Week 1-2** | Project setup, CI/CD, database schema, auth system, RBAC, multi-tenant foundation, design system |
| **Week 3-4** | Student Information System (profiles, search, bulk import), School configuration, Grades/Sections/Subjects setup |

#### Month 2: ERP Core Modules

| Week | Deliverables |
|---|---|
| **Week 5-6** | Attendance Management (daily marking, reports, parent notifications), Fee Management (structure, invoices, online payment with Razorpay) |
| **Week 7-8** | Timetable Management (create, view), Exam Management (schedule, marks entry, grade calculation), Basic Report Cards |

#### Month 3: AI Copilot MVP + Communication

| Week | Deliverables |
|---|---|
| **Week 9-10** | AI Lesson Planner (daily plans), AI Test Generator (basic), Curriculum DB (CBSE Classes 6-12 core subjects) |
| **Week 11-12** | Parent Communication (SMS + in-app notifications), Parent Portal MVP (attendance, fees, homework view), Basic Admin Dashboard |

#### Phase 1 Feature Checklist

```
ERP:
[x] School setup & configuration
[x] Student profiles + bulk import
[x] Daily attendance (mark + view)
[x] Absence notifications to parents (SMS)
[x] Fee structure + invoice generation
[x] Online fee payment (Razorpay UPI/Card)
[x] Fee receipts + payment history
[x] Class timetable (create + view)
[x] Exam schedule + marks entry
[x] Grade calculation
[x] Basic report cards (PDF)
[x] Staff profiles
[x] Staff leave management (apply + approve)

AI Copilot:
[x] AI Lesson Plan Generator (daily plans, CBSE)
[x] AI Test Generator (MCQ + short answer)
[x] Curriculum Database (CBSE, Classes 6-12, Math/Science/English)

Communication:
[x] SMS notifications (attendance, fees)
[x] In-app announcements

Parent Portal:
[x] Mobile web (responsive)
[x] View attendance
[x] View pending fees + pay online
[x] View exam results
[x] View announcements

Infrastructure:
[x] Multi-tenant architecture
[x] Authentication + RBAC
[x] Responsive web app
[x] Basic monitoring & logging
```

---

### Phase 2: Growth (Months 4-6)

> **Goal**: Full LMS, advanced AI Copilot, Parent App, WhatsApp integration

#### Month 4: LMS + Advanced AI Copilot

| Deliverables |
|---|
| Digital Content Library (upload, organize, share) |
| Homework Management (create, submit, grade) |
| AI Worksheet Generator |
| AI Homework Generator |
| AI Report Card Comment Assistant |
| AI Parent Communication Assistant |
| Curriculum DB expansion (ICSE, more subjects) |

#### Month 5: Parent Experience + Student Tutor

| Deliverables |
|---|
| Parent Mobile App (React Native — iOS + Android) |
| WhatsApp Integration (automated messages) |
| AI Student Tutor MVP (Explain + Doubt Solver) |
| AI Quiz Generator for Students |
| RAG Pipeline (NCERT content indexed) |
| Period-wise attendance |

#### Month 6: Analytics + Polish

| Deliverables |
|---|
| Student Analytics Dashboard |
| Teacher Analytics Dashboard |
| Principal Executive Dashboard |
| Parent Weekly AI Summary |
| Assignment Management |
| Admission Management (online form, pipeline) |
| Advanced Report Cards (templates, co-scholastic) |
| Email notifications |

#### Phase 2 Feature Checklist

```
LMS:
[x] Content Library
[x] Homework management (assign, submit, grade)
[x] Lesson Plan management (with AI + coordinator review)
[x] Assignment management
[x] Curriculum coverage tracking

AI Copilot (Advanced):
[x] AI Worksheet Generator (Practice, Revision, HOTS)
[x] AI Homework Generator (with personalization)
[x] AI Report Card Comments (bulk generation)
[x] AI Parent Communication drafts
[x] Multi-chapter test papers
[x] Answer key generation

AI Student Tutor:
[x] AI Explain (6 modes)
[x] AI Doubt Solver (text input)
[x] AI Quiz Generator
[x] Session management

Analytics:
[x] Student performance trends
[x] Class performance analytics
[x] Principal dashboard (school health)
[x] Parent child progress view

Communication:
[x] WhatsApp integration
[x] Email integration
[x] Push notifications (mobile)
[x] Circulars with acknowledgement

Parent:
[x] Native mobile app (iOS + Android)
[x] WhatsApp bot (basic commands)
[x] Weekly AI progress summary
[x] Leave application

ERP Extensions:
[x] Admission management
[x] Period-wise attendance
[x] Advanced report cards
[x] Teacher timetable view
```

---

### Phase 3: Advanced AI + Scale (Months 7-12)

> **Goal**: Full AI platform, multi-school support, predictive analytics, advanced features

#### Months 7-8: Advanced AI

| Deliverables |
|---|
| AI Practice Mode (adaptive difficulty) |
| AI Study Planner |
| AI Revision Assistant (flashcards, summaries) |
| AI Exam Preparation (mock tests) |
| Doubt Solver with image upload (OCR) |
| AI question quality analysis |
| Advanced RAG with source attribution |

#### Months 9-10: Multi-School + Predictive

| Deliverables |
|---|
| Multi-school management dashboard |
| Cross-campus benchmarking |
| At-risk student prediction |
| Board exam prediction |
| Standardization tools for school chains |
| State Board curriculum support (2-3 states) |
| Biometric attendance integration |

#### Months 11-12: Enterprise + Polish

| Deliverables |
|---|
| Transfer certificate generation |
| Promotion workflows |
| Payroll integration (export) |
| Room allocation optimization |
| AI-powered substitution suggestions |
| Advanced parent AI assistant (conversational) |
| Offline mode for critical workflows |
| Multilingual support (Hindi) |
| Performance optimization |
| SOC 2 compliance preparation |
| Enterprise security features |

#### Phase 3 Feature Checklist

```
AI (Advanced):
[x] Adaptive practice mode
[x] AI Study Planner
[x] Revision packages (summaries, flashcards)
[x] Mock test generator + auto-evaluation
[x] Image-based doubt solving (OCR)
[x] Question quality analytics
[x] Source attribution in RAG
[x] AI answer evaluation

Multi-School:
[x] School group management
[x] Cross-campus analytics
[x] Benchmarking dashboard
[x] Standardization tools

Predictive Analytics:
[x] At-risk student detection
[x] Board exam prediction
[x] Attendance trend prediction
[x] Fee collection prediction

ERP (Advanced):
[x] Transfer certificates
[x] Promotion workflows
[x] Payroll data export
[x] Substitution management
[x] Room allocation
[x] Biometric integration

Platform:
[x] Offline mode
[x] Hindi language support
[x] Enterprise security
[x] API for third-party integrations
```

---

## 2. Development Estimates

### Phase 1 (Months 1-3): ~3,600 person-hours

| Module | Estimated Effort | Team |
|---|---|---|
| Infrastructure + Auth | 200 hours | Backend + DevOps |
| Design System + UI Framework | 160 hours | Frontend + Design |
| Student Information System | 240 hours | Backend + Frontend |
| Attendance Management | 160 hours | Backend + Frontend |
| Fee Management | 320 hours | Backend + Frontend + Payment |
| Timetable Management | 120 hours | Backend + Frontend |
| Exam Management | 280 hours | Backend + Frontend |
| Report Cards | 160 hours | Backend + Frontend |
| Staff Management | 120 hours | Backend + Frontend |
| AI Lesson Planner | 200 hours | AI + Backend |
| AI Test Generator | 240 hours | AI + Backend |
| Curriculum Database (CBSE) | 320 hours | AI + Content |
| Parent Communication (SMS) | 80 hours | Backend |
| Parent Portal (Web) | 200 hours | Frontend |
| Admin Dashboard | 120 hours | Frontend |
| Testing & QA | 400 hours | QA |
| Project Management | 200 hours | PM |
| **Total** | **~3,520 hours** | |

### Phase 2 (Months 4-6): ~4,800 person-hours
### Phase 3 (Months 7-12): ~8,000 person-hours

### Total Year 1: ~16,000 person-hours

---

## 3. Non-Functional Requirements

| Requirement | Target | Measurement |
|---|---|---|
| **Availability** | 99.9% uptime | Monthly monitoring |
| **Response Time** | <500ms for API (P95) | APM monitoring |
| **AI Response Time** | <5s for generations (P95) | Custom tracking |
| **Concurrent Users** | 10,000 per school, 500K total | Load testing |
| **Data Storage** | 100GB per school (5 year) | Storage monitoring |
| **Page Load Time** | <3s (first load), <1s (subsequent) | Lighthouse |
| **Mobile Performance** | Lighthouse score >80 | Automated testing |
| **Backup** | Daily automated, 30-day retention | Automated verification |
| **Recovery** | RPO: 1 hour, RTO: 4 hours | DR testing quarterly |
| **Security Scan** | Zero critical/high vulnerabilities | Weekly automated scans |
| **Browser Support** | Chrome, Firefox, Safari, Edge (last 2 versions) | Cross-browser testing |
| **Mobile Support** | iOS 15+, Android 10+ | Device testing |
| **Localization** | English (P0), Hindi (P1), Regional (P2) | Manual verification |
| **Accessibility** | WCAG 2.1 AA | Automated + manual audit |

---

## 4. Risks & Mitigation

| # | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **AI hallucination in academic content** | Medium | Critical | RAG with source attribution, teacher review before publish, factual validation layer |
| 2 | **LLM API outages** | Medium | High | Multi-provider setup (OpenAI + Gemini + fallback), response caching, graceful degradation |
| 3 | **LLM cost overrun** | High | Medium | Response caching, model tiering, usage quotas per school, cost monitoring alerts |
| 4 | **Poor AI adoption by teachers** | Medium | High | Intuitive UX, minimal clicks, training programs, show time-saved metrics, gradual rollout |
| 5 | **Data breach / privacy violation** | Low | Critical | Encryption, RBAC, RLS, audit logs, penetration testing, SOC 2 compliance |
| 6 | **Scaling issues during exam season** | Medium | High | Auto-scaling, load testing (2x peak), database optimization, CDN for static content |
| 7 | **Curriculum data quality issues** | Medium | High | Expert review process, automated validation, teacher feedback loop |
| 8 | **School internet connectivity** | High | Medium | Offline mode for critical features, progressive enhancement, low-bandwidth optimization |
| 9 | **Payment gateway failures** | Low | High | Multiple payment options, retry mechanism, manual payment recording |
| 10 | **Competitor feature parity** | Medium | Medium | Focus on AI differentiation, fast iteration, customer feedback loops |
| 11 | **DPDP Act compliance** | Medium | High | Privacy-by-design, consent management, data minimization, legal review |
| 12 | **Feature scope creep** | High | Medium | Strict MVP boundaries, phase-gate approach, weekly prioritization reviews |
| 13 | **Teacher resistance to AI** | Medium | High | Position as assistant (not replacement), show time savings, gradual introduction |
| 14 | **Student misuse of AI tutor** | Medium | Medium | Usage limits, topic restriction, parent monitoring, anti-manipulation guardrails |
| 15 | **Integration complexity (WhatsApp, biometric, payment)** | Medium | Medium | Dedicated integration service, adapter pattern, staging environment testing |

---

## 5. Competitive Differentiators Summary

| vs. Legacy ERPs (Fedena, Skolaro, CampusCare) | vs. AI Learning Tools (Byju's, Khan Academy) | vs. Communication Apps (ClassDojo, Bloomz) |
|---|---|---|
| ✅ AI-native (not bolt-on) | ✅ Full ERP (not just learning) | ✅ Full ERP + LMS (not just communication) |
| ✅ Modern tech stack (cloud-native) | ✅ Curriculum-aligned to Indian boards | ✅ AI-powered insights |
| ✅ AI Teacher Copilot | ✅ School workflow integration | ✅ Fee management + payment |
| ✅ AI Student Tutor | ✅ Teacher tools (not just student) | ✅ Exam management + report cards |
| ✅ Predictive analytics | ✅ Admin + operations features | ✅ Multi-school support |
| ✅ WhatsApp-native parent engagement | ✅ Parent engagement | ✅ Curriculum-aware AI |
| ✅ Multi-school benchmarking | ✅ Affordable SaaS pricing | ✅ WhatsApp + SMS + Push |

---

## 6. UI/UX Flow Summary

### Key User Flows

| Flow | Steps | Target Time |
|---|---|---|
| **Teacher marks attendance** | Open app → Class auto-selected → Toggle absent → Submit | <2 minutes |
| **Teacher generates test paper** | Select params → Generate → Preview → Edit (optional) → Export PDF | <5 minutes |
| **Teacher generates lesson plan** | Select chapter → Generate → Review → Save | <3 minutes |
| **Teacher generates report comments** | Open class → Generate all → Review → Approve | <15 min (40 students) |
| **Parent pays fees** | Open app → View pending → Pay Now → UPI/Card → Receipt | <2 minutes |
| **Parent checks attendance** | Open app → Dashboard shows today's status → Tap for calendar | <30 seconds |
| **Student asks a doubt** | Open AI Tutor → Type doubt → Get explanation → Ask follow-up | <1 minute to first response |
| **Admin creates exam** | Define exam → Set schedule → Publish → Wait for marks → Calculate | <10 minutes setup |
| **Admin enrolls student** | Admission form → Review → Approve → Pay → Assign class | <5 minutes |

### Design System Principles

1. **Minimal Clicks**: Most common actions (mark attendance, view dashboard) in ≤2 clicks
2. **Smart Defaults**: Auto-select today's date, teacher's class, current academic year
3. **Progressive Disclosure**: Show summary first, details on demand
4. **Consistent Patterns**: Same interaction model across modules
5. **Visual Hierarchy**: Important actions prominent, secondary actions accessible
6. **Loading States**: Skeleton screens, not spinners
7. **Error Prevention**: Validation before submission, confirmation for destructive actions
8. **Responsive**: Web app works on tablets (common in Indian schools)

---

## 7. Success Metrics (Year 1)

| Metric | Target |
|---|---|
| Schools onboarded | 50-100 |
| Total students on platform | 25,000-50,000 |
| Monthly active teachers using AI Copilot | 60% |
| Teacher time saved per week | 8-10 hours |
| Report card generation time (vs. manual) | 90% reduction |
| Parent app monthly active rate | 70% |
| Fee collection rate improvement | 15-25% |
| AI tutor student engagement | 40% weekly active |
| Platform uptime | 99.9% |
| NPS (Net Promoter Score) | >50 |
| MRR (Monthly Recurring Revenue) | ₹10-25L |

---

*This completes the AI2School Master Product Design Document.*

## Document Index

| # | Document | Description |
|---|---|---|
| 00 | [Executive Summary](./00-executive-summary.md) | Product vision, market positioning, team structure |
| 01 | [User Personas](./01-user-personas.md) | 8 detailed personas + RBAC permission matrix |
| 02 | [Module 1: School ERP](./02-module-erp.md) | SIS, Attendance, Fees, Timetable, Exams, Staff, Communication |
| 03 | [Module 2: LMS](./03-module-lms.md) | Content Library, Lesson Plans, Homework, Assignments, Progress |
| 04 | [Module 3: AI Teacher Copilot](./04-module-ai-teacher-copilot.md) | 6 AI tools with prompts, workflows, guardrails |
| 05 | [Module 4: AI Student Tutor](./05-module-ai-student-tutor.md) | 7 AI features with adaptive algorithms |
| 06 | [Module 5: AI Analytics](./06-module-ai-analytics.md) | 4 dashboards with AI-powered insights |
| 07 | [Module 6: Parent Portal](./07-module-parent-portal.md) | App design, WhatsApp integration, AI assistant |
| 08 | [AI Architecture](./08-ai-architecture.md) | 6 agents, RAG, curriculum intelligence, LLM strategy |
| 09 | [Technical Architecture](./09-technical-architecture.md) | Tech stack, schema, API, security, SaaS design |
| 10 | [MVP Roadmap](./10-mvp-roadmap.md) | 3-phase roadmap, estimates, risks, success metrics |
