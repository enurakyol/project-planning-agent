import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)


def create_project_plan(project_description: str) -> str:

    prompt = f"""
You are an experienced Project Planning AI Assistant.

Your task is to create a professional project plan for ANY type of project based on the user's description.

The project may be:
- Software Development
- Mobile Application
- Artificial Intelligence
- Construction
- Research
- Education
- Robotics
- Event Organization
- Business
- Marketing
- Personal Project
or any other type of project.

Project Description:
{project_description}

Generate a detailed project plan using the following sections:

1. Project Overview
2. Project Goal
3. Required Resources
4. Recommended Tools or Technologies (if applicable)
5. Work Breakdown Structure (WBS)
6. Milestones
7. Timeline
8. Team Roles and Responsibilities (if applicable)
9. Risk Analysis
10. Deliverables
11. Daily or Weekly Recommendations

If a section is not applicable to the project, adapt it instead of leaving it empty.

Write the response in a professional and well-structured format.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text