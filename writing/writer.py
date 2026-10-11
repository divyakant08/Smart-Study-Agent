from google.adk.agents import Agent

writer_agent = Agent(
    name="writer_agent",
    model="gemini-3.5-flash-lite",
    instruction="""
    Combine outputs from topic_analysis, practice_plan, and schedule_plan into one complete study plan.
    If review_feedback exists in session state, refine and improve the plan accordingly.
    Ensure inclusion of day-wise schedule, topics, practice, revision, and mock test preparation.
    """,
    output_key="study_plan_draft"
)