from langchain_ollama import OllamaLLM
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
import os

def create_data_analyzer(model_name="gemma2:9b", csv_path=None):
    """
    Creates a data analysis agent using Ollama and LangChain.
    
    Args:
        model_name (str): Name of the Ollama model to use
        csv_path (str): Path to the CSV file to analyze
    
    Returns:
        agent: LangChain agent for data analysis
    """
    # Initialize Ollama
    llm = OllamaLLM(
        model=model_name,
        temperature=0.1
    )
    
    # Load the CSV file
    if csv_path and os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        raise FileNotFoundError("Please provide a valid CSV file path")
    
    # Create the agent
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type="zero-shot-react-description",
        allow_dangerous_code=True,
    )
    
    return agent, df

def analyze_data(agent, query):
    """
    Run analysis queries using the agent.
    
    Args:
        agent: LangChain agent for data analysis
        query (str): Question or analysis request
    """
    try:
        response = agent.invoke({"input": query})
        return response.get('output', '')

    except Exception as e:
        return f"Error during analysis: {str(e)}"

def main():
    # File path
    csv_path = r"C:\Users\karthik.muthuswamy\OneDrive - Accenture\Documents\GeilBrau.csv"
    
    # Create the analyzer
    try:
        agent, _ = create_data_analyzer(csv_path=csv_path)
        
        print("\nMissing Values Analysis:")
        missing_analysis = analyze_data(agent, "Analyze the missing values in this dataset and suggest appropriate methods for handling them.")
        print(missing_analysis)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
