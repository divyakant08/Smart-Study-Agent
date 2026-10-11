from google.adk.agents import Agent

practice_agent = Agent(
    name="practice_agent",
    model="gemini-3.5-flash-lite",
    instruction="""
    Decide how much practice should be done for each topic based on current level.
    Specify problem counts (e.g., Arrays -> 5 problems) and type of practice:
    - Concept Questions
    - Coding Problems
    - Mixed Practice
    - Mock Test
    """,
    output_key="practice_plan"
)