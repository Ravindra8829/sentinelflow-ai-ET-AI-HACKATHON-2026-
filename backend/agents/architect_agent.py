from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def architect_plan(goal):

    prompt = f"""
    Break the following enterprise goal into workflow steps:

    Goal: {goal}

    Return numbered steps.
    """

    return llm.invoke(prompt)
