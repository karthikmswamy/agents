"""
Script to create an agent for generating step-by-step documentation for creating an API key on Google AI Studio.
This script runs using an API key from Google AI Studio.
Ensure the following environment variables are set:
- GEMINI_API_KEY
"""

import os
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.environ["GEMINI_API_KEY"],
)

info_agent = Agent(
    role="Documentation Agent",
    goal="Create step-by-step comprehensive documentation on the given topic",
    backstory="""You are an agent that provides detailed answers.
    Your documentation wins quality awards.""",
    llm=llm,
)

agent_task = Task(
    description="Create an API key on Google AI Studio",
    expected_output="Give a summary and a detailed answer as bullet points.",
    agent=info_agent,
    verbose=True,
    output_file="output.md",
)

crew = Crew(
    agents=[info_agent],
    tasks=[agent_task],
    verbose=True,
)

result = crew.kickoff()

print("Results")
print(result)
