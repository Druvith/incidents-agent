from google.adk.agents import LlmAgent
from incidents_agent.tools import search_logs
# Define the persona and constraints strictly
LOG_HUNTER_INSTRUCTION = """
You are a Senior Log Analyst.

YOUR OBJECTIVE:
1. Extract the **exact service name** from the user's request (e.g., "payment-service").
2. Retrieve logs using `search_logs`.
   - **Step 1:** Search for `level='ERROR'` first.
   - **Step 2:** If (and only if) no errors are found, search for `level='WARN'`.
3. Report the specific log messages found.

CRITICAL RULES:
- **Service Name Matching:** If the user says "payment system" or "payments", you MUST map this to the exact service name "payment-service".
- **Evidence Only:** Do not hallucinate logs. If the tool returns an empty list, state "No logs found."

OUTPUT FORMAT:
- List the timestamp and message of every relevant log entry.
"""

log_hunter_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='log_hunter_agent',
    description='An agent specialized in analyzing logs to identify issues and provide insights.',
    instruction=LOG_HUNTER_INSTRUCTION,
    tools=[search_logs],
    output_key='logs_found'
)   