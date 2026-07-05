# AI Project Planning Agent

An AI-powered Project Planning Agent developed with Python and Google Gemini. The agent analyzes a natural language project description and generates a complete, structured project plan for various project types such as software, AI, engineering, education, research, business, and event management.

---

# Project Overview

This project demonstrates how a Large Language Model (LLM) can be used as an intelligent project planning assistant.

Instead of manually preparing a project plan, users simply describe their project in natural language. The agent analyzes the request and generates a professional project plan including goals, milestones, timeline, risks, required resources, deliverables, and recommendations.

---

# Features

- AI-powered project planning
- Supports multiple project types
- Generates structured project documentation
- Creates Work Breakdown Structure (WBS)
- Generates milestones and project timeline
- Performs risk analysis
- Suggests required resources
- Recommends tools and technologies
- Provides daily and weekly recommendations

---

# Project Architecture

```
                User
                  │
                  ▼
             main.py
                  │
                  ▼
           planner.py
                  │
                  ▼
         Google Gemini API
                  │
                  ▼
      AI Generated Project Plan
```

---

# Project Workflow

1. The user enters a project description.
2. The application creates a structured AI prompt.
3. The prompt is sent to Google Gemini.
4. Gemini analyzes the project requirements.
5. A detailed project plan is generated.
6. The generated plan is displayed to the user.

---

# Technologies

- Python
- Google Gemini API
- Google GenAI SDK
- python-dotenv

---

# Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/project-planning-agent.git
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application.

```bash
python main.py
```

---

# Example Input

```
Plan a Charity Event
```

or

```
Develop a Hospital Management System
```

or

```
Design an Autonomous Drone
```

---

# Example Output

The generated project plan includes:

- Project Overview
- Project Goal
- Required Resources
- Recommended Tools
- Work Breakdown Structure
- Milestones
- Timeline
- Team Roles
- Risk Analysis
- Deliverables
- Daily / Weekly Recommendations

---

# Future Improvements

- Export project plans as PDF
- Save project history
- Web interface
- Multi-language support
- Interactive planning mode

---

# Author

**Elif Nur Akyol**