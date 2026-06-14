# AI2School MVP 🚀

Welcome to the AI2School MVP! This repository contains a modern, multi-tenant school ERP built with a "Design-from-day-1" and "i18n-from-day-1" philosophy. 

## Tech Stack
- **Backend**: Python, FastAPI, SQLAlchemy 2.0 (Async), PostgreSQL, Alembic
- **Frontend**: React 19, Vite, TypeScript, Tailwind CSS v4, Zustand, TanStack Query

---

## 🛠️ How to Test the Application Locally

Follow these steps to spin up the entire application locally and test the features we've built so far.

### 1. Start the Database (PostgreSQL)
Ensure you have Docker and Docker Compose installed and running.
```bash
# From the root directory
docker compose up -d
```
*This will start a PostgreSQL instance (`ai2school-postgres`) exposed on port 5432.*

### 2. Start the Backend API (FastAPI)
Open a new terminal window and navigate to the backend folder to start the API.

```bash
cd backend

# 1. Activate the virtual environment
source venv/bin/activate

# 2. (First-time only) If you haven't run the seed script yet or your DB is empty,
# run the seed script to create a dummy school and superadmin user:
python scripts/seed.py

# 3. Start the FastAPI development server
fastapi dev app/main.py --port 8000
```
*The API is now running at `http://localhost:8000`. You can view the automatic Swagger UI docs at `http://localhost:8000/api/v1/openapi.json`.*

### 3. Start the Frontend Application (React)
Open another terminal window and navigate to the frontend folder.

```bash
cd frontend

# Start the Vite development server
npm run dev
```
*The frontend is now running at `http://localhost:5173`. Vite will automatically proxy API requests to `http://localhost:8000/api`.*

---

## 🧪 What to Test

Now that everything is running, open `http://localhost:5173` in your browser. Here is what you can test right now:

### 1. Authentication & JWT Flow
1. You should be redirected to the **Login** screen (`/login`).
2. Log in using the seeded credentials:
   - **Email**: `admin@ai2school.com`
   - **Password**: `password`
3. Upon success, you will see the loading state on the button, the JWT token will be securely stored via Zustand, and you'll be redirected to the **Dashboard**.

### 2. Application Shell & Routing
1. Test the **Sidebar Navigation**: Navigate between "Dashboard", "Students", and "Courses". Notice the smooth transitions and protected routing framework.
2. In the **Header**, you should see the email of the logged-in user (`admin@ai2school.com`).
3. Test the **Logout** button. It will clear your session and safely boot you back to the login page.

### 3. School Configurations (Courses)
1. Navigate to the **Courses** page using the sidebar.
2. Click **"Add Course"**. 
3. Because our system is built with i18n out-of-the-box, the form will ask you for both an **English Name** (e.g., Mathematics) and a **Hindi Name** (e.g., गणित).
4. Enter a Course Code (e.g., `MATH101`) and hit **Save Course**.
5. TanStack Query will automatically hit our FastAPI backend (`POST /api/v1/school/subjects`), validate the Pydantic schema, save it in PostgreSQL, and instantly refresh the UI table without requiring a page reload!
