from google.adk.agents import Agent

topic_agent = Agent(
    name="topic_agent",
    model="gemini-3.5-flash-lite",
    instruction="""
    Analyze the topics provided by the student.
    For each topic, identify:
    - Priority: High / Medium / Low
    - Difficulty level
    - Recommended study focus
    """,
    output_key="topic_analysis"
)