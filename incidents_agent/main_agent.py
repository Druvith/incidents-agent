from google.adk.agents import SequentialAgent
from subagents.dispatcher import dispatcher_agent
from subagents.synthesizer import synthesizer_agent

incident_response_team = SequentialAgent(
    name='incident_response_team',
    description='An incident response agent that coordinates sub-agents to analyze incidents and produce a root cause analysis report.',
    steps=[dispatcher_agent, synthesizer_agent],
)

root_agent = incident_response_team

