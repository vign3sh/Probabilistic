from agents.agent_optimal import Agent


def get_agent(type):
    if type == Agent.get_agent_type():
        return Agent