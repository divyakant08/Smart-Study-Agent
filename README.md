# 📚 SmartStudyAgent — AI-Powered Study Planner

> An intelligent multi-agent system built with **Google Agent Development Kit (ADK) + Gemini** that generates personalized, day-wise exam study plans for students.

---

## 📌 Overview

**SmartStudyAgent** is an AI-powered study planning assistant built using the **Google ADK** framework and the **Gemini 3.5 Flash Lite** model.

### What Problem Does It Solve?

During exam preparation, students have to manually plan:
- Which topics to study first?
- How much practice to do for each topic?
- How to create a day-wise schedule?
- When to revise and take mock tests?

**SmartStudyAgent** handles all of this automatically — the student simply provides their subject, topics, exam date, and available study time, and the AI agents collaboratively generate a complete study plan!

### How It Works (High-Level Flow)

```
Student Input → Coordinator → Planning → Parallel Analysis → Writing + Review Loop → Final Study Plan
```

---

## ✨ Key Features

### Multi-Agent Architecture

SmartStudyAgent consists of **7 specialized AI agents** that use 3 different workflow patterns:

| Agent | Role | Output Key |
|-------|------|------------|
| **Coordinator Agent** | Extracts key details from the student's request (subject, exam date, topics, level, study time) | `student_info` |
| **Planning Agent** | Prepares requirements for the analysis phase | `planning_requirements` |
| **Topic Agent** | Analyzes each topic's priority (High/Medium/Low) and difficulty level | `topic_analysis` |
| **Practice Agent** | Determines practice type and problem count for each topic | `practice_plan` |
| **Schedule Agent** | Converts available time and remaining days into a day-wise schedule | `schedule_plan` |
| **Writer Agent** | Combines all analysis outputs into a complete study plan | `study_plan_draft` |
| **Reviewer Agent** | Reviews the plan for topic coverage, time fit, practice, and revision | `review_feedback` |

### Workflow Patterns Used

| Pattern | Agents | Description |
|---------|--------|-------------|
| **Sequential** (Root) | Coordinator → Planning → Analysis → Refinement | Agents run one after another in order |
| **Parallel** | Topic + Practice + Schedule (simultaneously) | All three analyzers run concurrently for speed |
| **Loop** (max 2 iterations) | Writer ↔ Reviewer | Writer drafts the plan, Reviewer provides feedback, then Writer refines it |

---

## 📁 Directory Structure

```
SmartStudyAgent/
│
├── __init__.py              # Package initializer — exposes the root agent
├── agent.py                 # 🏠 Root Agent — defines Sequential, Parallel, Loop workflows
├── coordinator.py           # 🎯 Coordinator Agent — parses the student's request
├── planning.py              # 📋 Planning Agent — prepares requirements for analysis
│
├── analyzers/               # 🔍 Parallel Analysis Agents (all three run concurrently)
│   ├── topic.py             #   → Topic priority & difficulty analyzer
│   ├── practice.py          #   → Practice type & problem count planner
│   └── schedule.py          #   → Day-wise schedule generator
│
├── writing/                 # ✍️ Writing & Review Loop (max 2 iterations)
│   ├── writer.py            #   → Study plan draft writer
│   └── reviewer.py          #   → Plan quality reviewer & feedback provider
│
├── requirements.txt         # 📦 Python dependencies (google-adk, python-dotenv, google-genai)
├── .env                     # 🔑 Environment variables (API Key) — NOT tracked by git
├── .gitignore               # 🚫 Files/folders ignored by git
└── .adk/                    # 💾 ADK session data (auto-generated, git-ignored)
    └── session.db
```

---

## ⚙️ Prerequisites & Environment Setup

### Requirements

- **Python 3.10+** (recommended: Python 3.12 or 3.14)
- **Google Gemini API Key** (available for free from [Google AI Studio](https://aistudio.google.com/))
- **pip** (Python package manager)

### Step 1: Clone / Navigate to the Repository

```bash
# If it's a git repository, clone it
git clone <your-repo-url>
cd SmartStudyAgent

# Or navigate directly
cd path/to/SmartStudyAgent
```

### Step 2: Create a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> ✅ Once activated, you will see a `(.venv)` prefix in your terminal — this means the virtual environment is active.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install the following 3 packages:

| Package | Purpose |
|---------|---------|
| `google-adk` | Google Agent Development Kit — multi-agent framework |
| `python-dotenv` | Loads environment variables from a `.env` file |
| `google-genai` | Google Generative AI client library |

---

## 🔑 Environment Variables Configuration

Create a `.env` file in the project root (if it doesn't already exist):

```env
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=your_google_api_key_here
```

### How to Get an API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click **"Get API Key"** in the left sidebar
4. Click the **"Create API Key"** button
5. Copy the key and paste it after `GOOGLE_API_KEY=` in your `.env` file

> ⚠️ **IMPORTANT:** Never share your API key publicly or commit it to git. The `.gitignore` file already ignores `.env`.

---

## 🚀 Usage & How to Run

### Run via ADK Web Interface (Recommended)

```bash
# Navigate to the PARENT directory of SmartStudyAgent
cd path/to/ADK_Web

# Start the ADK Web UI
adk web
```

Your browser will open `http://localhost:8000`. From there:
1. Select **SmartStudyAgent** from the agent dropdown
2. Type your study request in the chat

### Run via ADK API Server

```bash
cd path/to/ADK_Web
adk api_server
```

The API server will start at `http://localhost:8000` for programmatic access.

### Example Input (Paste into the chat)

```
I have a Data Structures exam in 7 days. I can study 4 hours per day.
Topics: Arrays, Linked Lists, Trees, Graphs, Dynamic Programming.
My current level: Intermediate in Arrays and Linked Lists, Beginner in Trees and Graphs, No knowledge of DP.
Please create a complete study plan for me.
```

### Expected Output

The agent will generate:
- ✅ **Topic Analysis** — Priority and difficulty for each topic
- ✅ **Practice Plan** — Number of problems and type of practice for each topic
- ✅ **Day-wise Schedule** — A detailed schedule with revision slots
- ✅ **Reviewed Study Plan** — A refined final plan after the Writer + Reviewer loop

---

## 🧪 Agent Workflow Execution Order

```
1. Coordinator Agent
   └── Parses the student's request
        ↓
2. Planning Agent
   └── Prepares requirements for analysis
        ↓
3. Parallel Analysis (all three run concurrently)
   ├── Topic Agent    → topic_analysis
   ├── Practice Agent → practice_plan
   └── Schedule Agent → schedule_plan
        ↓
4. Refinement Loop (max 2 iterations)
   ├── Writer Agent   → study_plan_draft (combines all analysis)
   └── Reviewer Agent → review_feedback (quality check)
        ↓
5. Final Study Plan Output ✅
```

---

## 🛠️ Tech Stack

| Technology | Version / Details |
|------------|-------------------|
| Python | 3.10+ |
| Google ADK | Agent Development Kit (SequentialAgent, ParallelAgent, LoopAgent) |
| Gemini Model | `gemini-3.5-flash-lite` |
| Environment | `python-dotenv` for `.env` management |

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork** this repository
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and test them
4. **Commit** with a descriptive message:
   ```bash
   git commit -m "feat: add new analyzer for weak topics"
   ```
5. **Push** and create a **Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Improvement Ideas

- [ ] Add a user interface (Streamlit / Gradio)
- [ ] Study progress tracking feature
- [ ] Multiple exam planning support
- [ ] PDF export for study plans
- [ ] Spaced repetition algorithm integration
- [ ] Support for more Gemini models (Pro, Ultra)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) — Multi-agent framework
- [Google Gemini](https://ai.google.dev/) — AI model powering all agents

---

> **Made with Google ADK + Gemini** | SmartStudyAgent — Your AI Study Buddy 🎓
