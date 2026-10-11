from google.adk.agents import Agent

reviewer_agent = Agent(
    name="reviewer_agent",
    model="gemini-3.5-flash-lite",
    instruction="""
    Review the study plan draft stored in session state. Verify:
    1. Are all topics covered?
    2. Does the plan fit within available study time?
    3. Is sufficient practice included?
    4. Is revision included?
    5. Is the final day suitable for exam preparation?
    
    Provide specific improvement suggestions in review_feedback if changes are required.
    """,
    output_key="review_feedback"
)