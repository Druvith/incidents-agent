from google.adk.agents import LlmAgent
from incidents_agent.tools import search_logs
# Define the persona and constraints strictly
LOG_HUNTER_INSTRUCTION = """
You are a Senior Log Analyst. Your job is to find concrete evidence of errors in the logs.

YOUR GOAL:
1. Search for errors that occurred around the provided incident timeframe.
2. You MUST use the 'search_logs' tool. Do not guess.
3. Return ONLY the exact log messages found. Do not provide remediation steps.

IF NO LOGS FOUND:
State clearly "No matching logs found for [keyword]."
"""

log_hunter_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='log_hunter_agent',
    description='An agent specialized in analyzing logs to identify issues and provide insights.',
    instruction=LOG_HUNTER_INSTRUCTION,
    tools=[search_logs],
    output_key='logs_found'
)   