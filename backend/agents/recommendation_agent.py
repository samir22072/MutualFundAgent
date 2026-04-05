from crewai import Agent
from pydantic import BaseModel, Field
from typing import List, Optional
from tools.fund_tools import search_mutual_funds
from prompts import RECOMMENDATION_AGENT_PROMPT

class RecommendedFund(BaseModel):
    fund_name: str
    risk_profile: str
    cagr_1_year: Optional[float] = None
    cagr_3_year: Optional[float] = None
    cagr_5_year: Optional[float] = None

class RecommendationOutput(BaseModel):
    status: str = Field(..., description="'success' or 'intent_not_supported'")
    recommendations: List[RecommendedFund] = Field(default_factory=list, description="List of recommended funds")

def create_recommendation_agent(llm) -> Agent:
    return Agent(
        role="Recommendation Engine",
        goal="Select the top mutual funds using the search tool based on the user's intent and criteria.",
        backstory=f"{RECOMMENDATION_AGENT_PROMPT}\nYour response MUST follow the RecommendationOutput schema. Do not include markdown code blocks or any other text.",
        tools=[search_mutual_funds],
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
