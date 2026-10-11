from google.adk.agents import SequentialAgent, ParallelAgent, LoopAgent

from .coordinator import coordinator_agent
from .planning import planning_agent
from .analyzers.topic import topic_agent
from .analyzers.practice import practice_agent
from .analyzers.schedule import schedule_agent
from .writing.writer import writer_agent
from .writing.reviewer import reviewer_agent


# 1. PARALLEL WORKFLOW
analysis_parallel = ParallelAgent(
    name="analysis_parallel_workflow",
    sub_agents=[
        topic_agent,
        practice_agent,
        schedule_agent
    ]
)


# 2. LOOP WORKFLOW (Maximum 2 Iterations)
refinement_loop = LoopAgent(
    name="refinement_loop_workflow",
    sub_agents=[
        writer_agent,
        reviewer_agent
    ],
    max_iterations=2
)


# 3. SEQUENTIAL WORKFLOW (Root Agent)
root_agent = SequentialAgent(
    name="smartstudy_root_agent",
    sub_agents=[
        coordinator_agent,
        planning_agent,
        analysis_parallel,
        refinement_loop
    ]
)