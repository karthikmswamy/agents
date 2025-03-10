#!/usr/bin/env python
import warnings
from datetime import datetime
from crew import OllamaCrew
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "Accenture",
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    try:
        OllamaCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
