# Mutual Fund Agent 🚀

A powerful multi-agent financial advisory platform built with CrewAI, FastAPI, and Next.js. This application uses specialized AI agents to analyze mutual fund performance, research market trends, and provide personalized investment advice.

---

## 🏗️ Project Structure

- **`backend/`**: FastAPI server hosting the multi-agent system powered by **CrewAI**.
- **`frontend/`**: Modern web interface built with **Next.js**, **Tailwind CSS**, and **TypeScript**.
- **`mutual_funds.db`**: SQLite database containing fund performance data and historical records.

---

## ⚡ Quick Start

### 1. Environment Variables
Create the necessary environment files based on the provided examples:

**Backend:**
```bash
cp backend/.env.example backend/.env
```
Edit `backend/.env` and add your `GOOGLE_API_KEY`.

**Frontend:**
```bash
# Note: The example file is named env.local.example
cp frontend/env.local.example frontend/.env.local
```

### 2. Database Setup
Initialize the SQLite database with sample mutual fund data:
```bash
cd backend
python data/db_setup.py
```

### 3. Application Setup

#### Backend Setup
```bash
# Navigate to backend (if not already there)
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```
The backend will be available at `http://localhost:8000`.

#### Frontend Setup
```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```
Open `http://localhost:3000` in your browser.

---

## 🤖 AI Agents

The platform utilizes a structured multi-agent workflow:
- **Performance Analyst**: Analyzes historical data and calculates risk/return metrics.
- **Research Specialist**: Scours market trends and fund holdings.
- **Advisory Agent**: Synthesizes data to provide actionable investment recommendations.

---

## 🛠️ Tech Stack

- **Backend**: Python, CrewAI, FastAPI, LangChain (Google Gemini)
- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Database**: SQLite
- **Documentation**: Markdown support for rich reporting
