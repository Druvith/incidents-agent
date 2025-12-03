from google.adk.agents import ParallelAgent
from incidents_agent.subagents.git_investigator import git_investigator_agent
from incidents_agent.subagents.log_hunter import log_hunter_agent
from incidents_agent.subagents.metrics_analyst import metrics_analyst_agent

dispatcher_agent = ParallelAgent(
    name='dispatcher_agent',
    description='An agent that dispatches tasks to specialized sub-agents (such as LogHunter, MetricsAnalyst and GitInvestigator) based on the nature of the incident reported by the user.',
    sub_agents=[log_hunter_agent, metrics_analyst_agent, git_investigator_agent],
)

