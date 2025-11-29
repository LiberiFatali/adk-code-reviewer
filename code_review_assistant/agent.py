"""
Main agent orchestration for the Code Review Assistant.

This module defines a comprehensive code review assistant that analyzes
Python code and provides detailed feedback through a multi-stage pipeline.
"""

from .config import config
from google.adk.agents import Agent, LoopAgent, SequentialAgent
from code_review_assistant.sub_agents.review_pipeline.code_analyzer import code_analyzer_agent
from code_review_assistant.sub_agents.review_pipeline.style_checker import style_checker_agent
from code_review_assistant.sub_agents.review_pipeline.test_runner import test_runner_agent
from code_review_assistant.sub_agents.review_pipeline.feedback_synthesizer import feedback_synthesizer_agent

from code_review_assistant.sub_agents.fix_pipeline.code_fixer import code_fixer_agent
from code_review_assistant.sub_agents.fix_pipeline.fix_test_runner import fix_test_runner_agent
from code_review_assistant.sub_agents.fix_pipeline.fix_validator import fix_validator_agent
from code_review_assistant.sub_agents.fix_pipeline.fix_synthesizer import fix_synthesizer_agent


# Create sequential pipeline
code_review_pipeline = SequentialAgent(
    name="CodeReviewPipeline",
    description="Complete code review pipeline with analysis, testing, and feedback",
    sub_agents=[code_analyzer_agent, style_checker_agent, test_runner_agent, feedback_synthesizer_agent],
)

# # Root agent - coordinates the review pipeline
# root_agent = Agent(
#     name="CodeReviewAssistant",
#     model=config.worker_model,
#     description="An intelligent code review assistant that analyzes Python code and provides educational feedback",
#     instruction="""You are a specialized Python code review assistant focused on helping developers improve their code quality.

#     When a user provides Python code for review:
#     1. Immediately delegate to CodeReviewPipeline and pass the code EXACTLY as it was provided by the user.
#     2. The pipeline will handle all analysis and feedback
#     3. Return ONLY the final feedback from the pipeline - do not add any commentary

#     When a user asks what you can do or asks general questions:
#     - Explain your capabilities for code review
#     - Do NOT trigger the pipeline for non-code messages

#     The pipeline handles everything for code review - just pass through its final output.""",
#     sub_agents=[code_review_pipeline],
#     output_key="assistant_response",
# )


# Create the fix attempt loop (retries up to 3 times)
fix_attempt_loop = LoopAgent(
    name="FixAttemptLoop",
    sub_agents=[
        code_fixer_agent,  # Step 1: Generate fixes
        fix_test_runner_agent,  # Step 2: Validate with tests
        fix_validator_agent,  # Step 3: Check success & possibly exit
    ],
    max_iterations=3,  # Try up to 3 times
)

# Wrap loop with synthesizer for final report
code_fix_pipeline = SequentialAgent(
    name="CodeFixPipeline",
    description="Automated code fixing pipeline with iterative validation",
    sub_agents=[
        fix_attempt_loop,  # Try to fix (1-3 times)
        fix_synthesizer_agent,  # Present final results (always runs once)
    ],
)


# Update root agent to include both pipelines
root_agent = Agent(
    name="CodeReviewAssistant",
    model=config.worker_model,
    description="An intelligent code review assistant that analyzes Python code and provides educational feedback",
    instruction="""You are a specialized Python code review assistant focused on helping developers improve their code quality.

    When a user provides Python code for review:
    1. Immediately delegate to CodeReviewPipeline and pass the code EXACTLY as it was provided by the user.
    2. The pipeline will handle all analysis and feedback
    3. Return ONLY the final feedback from the pipeline - do not add any commentary

    After completing a review, if significant issues were identified:
     - If the user responds yes or requests fixes after you offer to help:
    * Delegate to CodeFixPipeline
    * Return the fix pipeline's complete output AS-IS

    When a user asks what you can do or general questions:
    - Explain your capabilities for code review and fixing
    - Do NOT trigger the pipeline for non-code messages

    The pipelines handle everything for code review and fixing - just pass through their final output.""",
    sub_agents=[code_review_pipeline, code_fix_pipeline],
    output_key="assistant_response",
)
