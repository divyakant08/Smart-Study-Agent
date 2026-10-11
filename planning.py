from google.adk.agents import Agent

planning_agent = Agent(
    name="planning_agent",
    model="gemini-3.5-flash-lite",
    instruction="""
    Prepare requirements for creating the study plan and trigger analysis for topic, practice, and schedule tasks.
    """,
    output_key="planning_requirements"
)