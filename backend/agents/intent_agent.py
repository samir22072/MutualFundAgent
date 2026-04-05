from crewai import Agent
from pydantic import BaseModel, Field
from typing import Optional
from prompts import INTENT_AGENT_PROMPT

class IntentOutput(BaseModel):
    intent: str = Field(..., description="'recommend_mutual_funds' or 'unsupported'")
    risk_profile: str = Field(description="The risk profile: 'low', 'medium', or 'high'", default="medium")
    investment_goal: str = Field(description="User's investment goal, e.g., 'wealth creation'", default="general growth")
    investment_horizon: str = Field(description="The investment duration, e.g., '1Y', '3Y', '5Y', or 'unknown'", default="unknown")
    original_query: str = Field(..., description="The exact original text of the user's query")

def create_intent_agent(llm) -> Agent:
    return Agent(
        role="Intent Identification Specialist",
        goal="Correctly identify if the user wants mutual funds and extract detailed preferences.",
        backstory=f"{INTENT_AGENT_PROMPT}\nYour output MUST be a valid JSON object only. No markdown code blocks, no conversational preamble. Your output must be JSON only. No markdown.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
