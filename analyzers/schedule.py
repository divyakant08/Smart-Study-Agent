from google.adk.agents import Agent

schedule_agent = Agent(
    name="schedule_agent",
    model="gemini-3.5-flash-lite",
    instruction="""
    Convert available study time and remaining exam days into a realistic day-wise schedule.
    Ensure to include revision and practice slots alongside new topics.
    """,
    output_key="schedule_plan"
)