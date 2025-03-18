# Agents Repository
This repo contains a set of use case specific agents that can be run locally (without an API key) or with a Google AI Studio API key.

## Prerequisite Software
The following are sofware and installations required for running these agents on your machine. Installation instructions for Windows and Mac are provided below:

### Windows
- Ollama - https://ollama.com/download/windows
- Python - https://www.python.org/downloads/windows/
- VS Code - https://code.visualstudio.com/Download

### Mac
- Ollama - https://ollama.com/download/mac
- Python - https://www.python.org/downloads/macos/
- VS Code - https://code.visualstudio.com/Download

## Prerequisite API key
The projects in this repo require you to create an API key that provides access to Gemini models.

- Create an API key on Google AI Studio - https://aistudio.google.com/apikey 

With the API key created, update the .env file with the environment variable as follows:
```
GEMINI_API_KEY=<your-api-key>
```

## Test your installations
Open a Terminal (Mac) or Command Prompt (Windows) and test the following:

```
ollama --version
> ollama version is 0.6.0

python --version
> Python 3.11.11

code --version
> 1.98.1
> 2fc07b811f760549dab9be9d2bedd06c51dfcb9a
> x64
```

## Pull an LLM to run locally
We will use two different models for this example, Llama and Gemma.
You can read more about both models here: 
- [Llama](https://www.llama.com/)
- [Gemma](https://ai.google.dev/gemma)

The models that we will be using for this example are:
- llama3.2:latest
- gemma3

From the command prompt opened above, run the following:
Note, you can quit from the ollama prompt by using the following command: `/bye`

```
ollama run llama3.2:latest
>>> Tell me about yourself
I'm an artificial intelligence model known as Llama. Llama stands for "Large Language Model Meta AI."

ollama run gemma3
>>> Tell me about yourself
Okay, let's talk about me! I'm Gemma, a large language model created by the Gemma team at Google DeepMind. I'm an open-weights model, which means I’m
publicly available for anyone to use and experiment with – a really exciting development in the AI world!

**Here's a breakdown of what I can do:**

* **I’m a language model:** This means I’ve been trained on a massive amount of text data. Because of this, I can understand and generate human-like text.
* **I can perform a wide variety of tasks:**
    * **Answering questions:** I can try to answer your questions in a comprehensive and informative way, even if they are open ended, challenging, or
strange.
    * **Creative writing:** I can generate different creative text formats, like poems, code, scripts, musical pieces, email, letters, etc.
    * **Summarization:** I can condense long pieces of text into shorter, more manageable summaries.
    * **Translation:** I can translate languages.
    * **Code generation:** I can generate code in various programming languages.
* **I have a specific size:** I come in different sizes – the smallest one is 2B parameters.  Larger models generally perform better, but require more
computational power.
* **I’m still under development:** I'm constantly being improved! The Gemma team is actively working on refining my abilities and addressing any
limitations.


**Important Note:**  Like all large language models, I have limitations:

* **I don't have real-time knowledge:** My training data has a cutoff point, so I won’t know about events that occurred after that date.
* **I can sometimes make mistakes:** I’m not perfect, and I can occasionally generate incorrect or misleading information. It’s always a good idea to
double-check my responses, especially for critical tasks.


**To help me understand what you’re looking for, could you tell me:**

*   What are you interested in talking about today?
*   Is there anything specific you’d like me to do (e.g., answer a question, write a story, etc.)?

I'm excited to chat with you! 😊
```

## Projects
The following are the projects and their descriptions:

- Basic Agent - a single script containing a single agent with a task and uses Gemini API. 
- Ollama Crew - a crew of agents built to perform competitor analysis using open weights models from Ollama, CrewAI, and LangChain.