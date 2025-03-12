"""
Script to create an agent for generating step-by-step documentation for creating an API key on Google AI Studio.
This script runs locally using Ollama.
Ensure the following models are available:
- llama3.2
- gemma3
"""

from time import time

from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

load_dotenv()


llm = LLM(
    # model='ollama/llama3.2',
    model="ollama/gemma3",
    base_url="http://localhost:11434",
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
    llm=llm,
)

start_time = time()
result = crew.kickoff()

print(result)
print(f"Agent run completed in {time() - start_time} seconds.")
