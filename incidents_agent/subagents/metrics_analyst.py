from google.adk.agents import LlmAgent
from incidents_agent.tools import get_recent_metrics

METRICS_ANALYST_INSTRUCTION = """
You are a Senior Site Reliability Engineer (SRE) specializing in observability.

YOUR OBJECTIVE:
1. Analyze the provided metrics to identify **anomalies**.
2. Specifically look for:
   - drastically increased Latency (ms).
   - high Error Rates (>1%).
   - CPU saturation (>80%).
3. Determine the EXACT timestamp when the metrics went from "Healthy" to "Unhealthy".

OUTPUT FORMAT:
- State the "Start Time" of the incident.
- List the peak values (e.g., "Latency peaked at 2400ms").
- If data is normal, state "System is healthy."
 """

metrics_analyst_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='metrics_analyst_agent',
    description='An agent specialized in analyzing system metrics to identify anomalies and provide insights.',
    instruction=METRICS_ANALYST_INSTRUCTION,
    tools=[get_recent_metrics],
    output_key='metrics_analysis'
)