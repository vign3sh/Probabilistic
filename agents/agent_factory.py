from agents.agent_optimal import AgentNew
from agents.agent import Agent


def get_agent(agent_type):
    if isinstance(agent_type, str):
        return AgentNew(int(agent_type.split("-")[1]))
    else:
        return Agent(agent_type)
