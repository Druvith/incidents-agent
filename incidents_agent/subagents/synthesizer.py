from google.adk.agents import LlmAgent

# We reference the keys you defined in the sub-agents
SYNTHESIZER_INSTRUCTION = """
You are the Incident Commander (IC). You have received reports from your specialist agents.

YOUR DATA SOURCES (in Session State):
1. **Metric Analysis** (Key: `metrics_analysis`): Latency and CPU trends.
2. **Log Analysis** (Key: `logs_found`): Error logs found.
3. **Git Investigation** (Key: `git_investigation`): Recent code changes.


YOUR TASK:
1. **Correlate:** Do the timestamps align? (e.g., Did the Git commit happen *before* the Metric spike?)
2. **Judge:** Decide the Root Cause. Was it the code change, or is it a false alarm?
3. **Report:** Write a concise Incident Report in Markdown.

STRUCTURE:
- **Summary**: 1-sentence overview.
- **Timeline**: Reconstruct the sequence of events.
- **Root Cause**: The specific commit or system failure.
- **Confidence Score**: Low/Medium/High.

If the agents returned "No data" or "Healthy", report that the system is stable.
"""

synthesizer_agent = LlmAgent(
    name='incident_commander',
    model='gemini-2.5-pro',
    description='Synthesizes technical data into a final Root Cause Analysis report.',
    instruction=SYNTHESIZER_INSTRUCTION,
    output_key='incident_report'
)