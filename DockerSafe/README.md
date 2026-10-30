# DockerSafe — Container Data Persistence & Disaster Recovery Simulator

**A Practical Docker Laboratory & Academic Demonstration Framework for College MCA / Computer Science Students**

[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.3-61dafb.svg)](https://react.dev/)
[![Docker SDK](https://img.shields.io/badge/Docker%20SDK-7.0+-2496ed.svg)](https://docker-py.readthedocs.io/)
[![Tests](https://img.shields.io/badge/tests-17%20passed-brightgreen.svg)](#testing)

---

## 1. Project Overview

### Problem Statement
Docker containers are useful for running isolated applications, but data stored only in a container's writable layer can be lost when the container is removed. Docker volumes and bind mounts provide persistent storage mechanisms, while backups provide another way to recover data after failures.

Students often learn these concepts theoretically without being able to observe the differences through repeatable experiments.

### Solution
**DockerSafe** is an interactive web-based Docker laboratory that connects to your local computer's real **Docker Engine** (via Docker Desktop) to orchestrate live **PostgreSQL 16 Alpine** database containers, named volumes, and backups. It measures:
- Data loss when containers are destroyed without persistent volumes.
- Zero-loss data survival across container lifecycles using Docker named volumes.
- Disaster recovery from independent logical SQL backups (`pg_dump`) after both the container and volume are obliterated.
- Host filesystem synchronization via host bind mounts.
- Exact recovery duration (in milliseconds), backup sizes, and SHA-256 cryptographic checksums.

---

## 2. Technology Stack

- **Frontend:** React 18, Vite, TypeScript, Tailwind CSS, Recharts, Lucide React.
- **Backend:** Python 3.13, FastAPI, Uvicorn, Docker SDK for Python (`docker`), SQLAlchemy 2.0.
- **Database:** Local SQLite (`data/dockersafe.db`) for experiment history, and official **PostgreSQL 16 Alpine** (`postgres:16-alpine`) for dynamic test containers.
- **Docker:** Docker Desktop on Windows, Docker Engine API, named volumes, host bind mounts.

---

## 3. Architecture

```
Host Computer (Windows Laptop)
 ├── Frontend (React + Vite) ───────> http://localhost:5173
 ├── Backend (FastAPI + Python) ────> http://127.0.0.1:8000
 ├── Application Metadata ──────────> SQLite (data/dockersafe.db)
 └── Logical Backups ───────────────> SQL files (data/backups/*.sql)
           │
           │ (Official Docker SDK for Python)
           ▼
 Docker Desktop Engine
  ├── Test PostgreSQL Containers ───> dockersafe-test-<run_id>
  └── Managed Named Volumes ────────> dockersafe-vol-<run_id>
```

---

## 4. Prerequisites

1. **Windows 10 / 11** with PowerShell.
2. **Python 3.11+** installed (Python 3.13 tested).
3. **Node.js v18+** installed (Node v26 tested).
4. **Docker Desktop for Windows** installed and running (configured for Linux containers).

---

## 5. Quick Start Installation & Execution

Open two PowerShell windows in `Y:\Docker Mini project` (or your project root).

### Terminal 1: Run the Backend API

```powershell
# 1. Navigate to backend directory
cd backend

# 2. Activate Python virtual environment
.\.venv\Scripts\Activate.ps1

# (Optional: install dependencies if setting up from scratch)
# pip install -r requirements.txt

# 3. Start the FastAPI backend server
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Backend will be accessible at:
- API Root: `http://127.0.0.1:8000`
- Interactive Swagger UI: `http://127.0.0.1:8000/docs`
- Health Endpoint: `http://127.0.0.1:8000/api/health`

---

### Terminal 2: Run the Frontend UI

```powershell
# 1. Navigate to frontend directory
cd frontend

# (Optional: install dependencies if setting up from scratch)
# cmd /c npm install

# 2. Start Vite development server
cmd /c npm run dev
```

Frontend will be accessible at:
- Web Dashboard: `http://localhost:5173`

---

## 6. How to Verify Docker Connectivity

Before running experiments, ensure Docker Desktop is started on your Windows machine:
```powershell
docker version
docker info
```

When Docker Desktop is running, DockerSafe will automatically detect it:
- The top-right status indicator in the dashboard will illuminate **green ("Docker Engine Ready v29.x")**.
- If Docker Desktop is stopped, a helpful warning banner appears with instructions to launch Docker Desktop and a **"Re-check Connection"** button.

---

## 7. How to Demonstrate to a Teacher or Examiner

Follow this step-by-step demonstration walkthrough for your college practical exam or viva presentation:

### Step 1: Open the Dashboard (`http://localhost:5173`)
Show the examiner the live system overview:
- Explain that DockerSafe is directly interfacing with the local Docker Engine.
- Point out the active container and volume counts.
- Explain the difference between stateless containers and stateful database workloads.

### Step 2: Demonstrate Experiment 1 (Ephemeral Data Loss)
1. Click **"Run Experiment 1"** (No Persistent Storage).
2. Point out the live stepper:
   - Notice the PostgreSQL test container starting without an attached volume.
   - Watch `pg_isready` verify database readiness.
   - Observe 20 synthetic records inserted and verified with `SELECT count(*)`.
   - Watch the container get terminated and recreated from the base image.
   - Point out the final query result: **0 records recovered, 20 records lost (100% data loss)**.
3. **Key Explanation to Teacher:** *"Stopping a container preserves its writable layer, but recreating a container wipes it completely. Without an external volume, database state is unrecoverable."*

### Step 3: Demonstrate Experiment 2 (Named Volume Persistence)
1. Click **"Run Experiment 2"** (Named Docker Volume).
2. Point out:
   - Creation of the named volume `dockersafe-vol-<id>` mounted at `/var/lib/postgresql/data`.
   - Insertion of 20 records.
   - The test container is **completely destroyed (`docker rm`)**, but the volume is retained.
   - A fresh container is started and attached to the existing volume.
   - Query result: **20 records recovered, 0 lost (100% data survival)** with exact recovery latency in milliseconds.
3. **Key Explanation to Teacher:** *"Docker volumes decouple persistent data from the container lifecycle. The data resides on the host storage engine outside the container's UnionFS layer."*

### Step 4: Demonstrate Experiment 3 (Backup & Disaster Recovery)
1. Click **"Run Experiment 3"** (Backup & Disaster Recovery).
2. Point out:
   - Insertion of records.
   - Generation of a real `pg_dump` logical backup stored in `data/backups/`.
   - Calculation of the SHA-256 cryptographic checksum.
   - **Catastrophic disaster simulation:** Both the container AND the volume are completely obliterated!
   - Provisioning of a brand-new volume and container.
   - Backup restoration via `psql` and verification of 100% record recovery.
3. **Key Explanation to Teacher:** *"Named volumes alone do not protect against accidental volume deletion or storage disk failure. Independent logical backups with checksum verification provide true disaster recovery."*

### Step 5: Show Comparison Analytics & Case Study Report
1. Click **"Comparison Analytics"** on the sidebar to show the grouped bar charts comparing data loss, record recovery, and latency.
2. Click **"Case Study Report"** on the sidebar to demonstrate the generated academic report:
   - Click **"Download Markdown"** or **"Download CSV"** to export the empirical data.
   - Click **"Print / PDF"** to display the academic paper formatting.

---

## 8. Resource Safety & Teardown

DockerSafe includes strict safeguards to prevent touching any unrelated containers or volumes on your machine:
- **Dedicated Labels:** All DockerSafe resources carry `dockersafe.managed=true`.
- **Pre-Deletion Checks:** Unlabeled resources will cause an immediate security violation error if targeted.
- **Resource Explorer:** Go to the **"Resource Explorer"** tab in the dashboard to inspect active test containers and click **"Clean All Lab Resources"** to safely remove all test artifacts.

---

## 9. Automated Testing

Run the automated backend test suite:
```powershell
cd backend
.\.venv\Scripts\pytest -v
```
All 17 tests (API validation, security guards, checksum validation, path traversal defense, and report generator) execute and pass in under 0.15 seconds.

---

## 10. Standalone Docker Compose Demo

A standalone `compose.yaml` is provided in the root directory as an independent reference:
```powershell
# Start PostgreSQL service with named volume
docker compose up -d

# Stop service while preserving persistent volume
docker compose down

# Stop service and delete volume (erases data)
docker compose down -v
```

---

## 11. Project Structure

```
DockerSafe/
├── frontend/                     # React 18 + Vite + TypeScript frontend
│   ├── src/
│   │   ├── components/           # Navbar, Sidebar, Modals, Status Banners
│   │   ├── pages/                # Dashboard, Experiments, History, Analytics, etc.
│   │   ├── services/api.ts       # Backend REST API client
│   │   └── types/index.ts        # TypeScript schemas
│   └── package.json
├── backend/                      # FastAPI Python backend
│   ├── app/
│   │   ├── main.py               # Application entrypoint & CORS
│   │   ├── api/endpoints.py      # REST endpoints (/docker, /experiments, /backups, etc.)
│   │   ├── core/config.py        # Settings & directory setup
│   │   ├── core/database.py      # SQLAlchemy & SQLite setup
│   │   ├── services/             # DockerService, ExperimentService, BackupService, ReportService
│   │   ├── models/               # SQLite database entities
│   │   └── schemas/              # Pydantic request/response schemas
│   ├── tests/                    # Pytest test suite (17 passed)
│   └── requirements.txt
├── data/
│   ├── backups/                  # Generated pg_dump .sql backup files
│   ├── bind_mounts/              # Bind mount experiment folders
│   └── dockersafe.db             # Local SQLite database
├── docs/
│   ├── ARCHITECTURE.md           # System architecture & Mermaid diagrams
│   ├── EXPERIMENTS.md            # Detailed experiment workflows & SQL
│   ├── TESTING.md                # Test execution record & results
│   └── CASE_STUDY.md             # Formal academic case study paper
├── compose.yaml                  # Optional standalone Compose demo
├── PROJECT_STATUS.md             # Implementation & verification checklist
├── .env.example                  # Environment configuration template
└── README.md                     # Comprehensive laboratory documentation
```

---

## 12. Troubleshooting

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| **"Docker Offline" in dashboard** | Docker Desktop is not running | Start Docker Desktop from your Start Menu. Wait until the Docker whale icon in the system tray becomes steady, then click "Re-check Connection". |
| **"Scripts disabled on this system"** | PowerShell script execution policy | Use `cmd /c npm ...` for npm commands or run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`. |
| **Port 8000 already in use** | Another local process using port 8000 | Run `uvicorn app.main:app --port 8080` and adjust the proxy in `frontend/vite.config.ts`. |
