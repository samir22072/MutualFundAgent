from crewai import Agent
from prompts import FORMATTER_AGENT_PROMPT

def create_formatter_agent(llm) -> Agent:
    return Agent(
        role="Financial Advisor Formatter",
        goal="Present the final mutual fund recommendations in a professional, human-readable format.",
        backstory=FORMATTER_AGENT_PROMPT,
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
