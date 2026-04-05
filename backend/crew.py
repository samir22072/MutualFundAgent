import os
from crewai import Crew, Task, LLM

from agents.intent_agent import create_intent_agent, IntentOutput
from agents.recommendation_agent import create_recommendation_agent, RecommendationOutput
from agents.formatter_agent import create_formatter_agent

def setup_crew(query: str):
    llm = LLM(
        model=f"gemini/{os.environ.get('GOOGLE_MODEL', 'gemini-2.5-flash-lite')}",
        temperature=float(os.environ.get("GOOGLE_TEMPERATURE", "0")),
        api_key=os.environ.get("GOOGLE_API_KEY")
    )
    
    intent_agent = create_intent_agent(llm)
    recommendation_agent = create_recommendation_agent(llm)
    formatter_agent = create_formatter_agent(llm)

    intent_task = Task(
        description=f"Analyze the following query: '{query}'. Extract the required entities. Your output must be a valid JSON object. Do not include markdown code blocks or any other text.",
        expected_output="A JSON object matching the IntentOutput schema.",
        agent=intent_agent,
        output_pydantic=IntentOutput
    )
    
    recommendation_task = Task(
        description="""Read the output of the intent task. If intent is unsupported, return status 'intent_not_supported'.
        Otherwise, use your search tool to find mutual funds matching the user's risk profile and horizon. 
        Select the top 3-5 best funds based on CAGR.
        Important: Your response must be an object satisfying the RecommendationOutput schema. Return only JSON.""",
        expected_output="A JSON object matching the RecommendationOutput schema.",
        agent=recommendation_agent,
        output_pydantic=RecommendationOutput,
        context=[intent_task]
    )
    
    formatter_task = Task(
        description="""Read the context from the previous tasks (intent and recommendations).
        Draft a final, high-quality markdown response as a professional Financial Advisor. 
        Politely decline if the intent is not supported.""",
        expected_output="A well-formatted markdown response string.",
        agent=formatter_agent,
        context=[intent_task, recommendation_task]
    )

    crew = Crew(
        agents=[intent_agent, recommendation_agent, formatter_agent],
        tasks=[intent_task, recommendation_task, formatter_task],
        verbose=True
    )
    
    return crew
