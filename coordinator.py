from google.adk.agents import Agent

coordinator_agent = Agent(
    name="coordinator_agent",
    model="gemini-3.5-flash-lite",
    instruction="""
    Receive the student's request and identify key details:
    - Subject
    - Exam date / Days remaining
    - Topics list
    - Current preparation level
    - Available study time per day
    
    Pass structured details to the planning workflow.
    """,
    output_key="student_info"
)