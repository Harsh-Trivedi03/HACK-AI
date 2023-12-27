from uagents import Agent, Context
from openai import api_requestor
from uagents.setup import fund_agent_if_low
import requests
import json

class PromptAgent(Agent):
    def __init__(self, name, seed):
        super().__init__(name=name, seed=seed)

    def process_prompt(self, job_requirements, resume_data):
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{
                "role": "user",
                "content": f"Match job requirement {job_requirements} with resumes {resume_data}"
            }],
            "temperature": 1.0,
            "top_p": 1.0,
            "n": 1,
            "stream": False,
            "presence_penalty": 0,
            "frequency_penalty": 0,
        }

        
        headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer UR-OPEN-AI-API-KEY-HERE"}

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response.json()

prompt_agent = PromptAgent("prompt", "prompt_seed")
# Example usage
job_requirements = {"position": "Web Developer", "tech_stacks": ["React", "NodeJS"], "experience": 3}
resume_data = {"resume1": "text1", "resume2": "text2", "resume3": "text3"}
best_match = prompt_agent.process_prompt(job_requirements, resume_data)
print(best_match)

prompt_agent_address = "http://127.0.0.1:8002/submit"
notification_agent_address = "notification_agent_address_here"
prompt_agent = PromptAgent("prompt_agent", "prompt_secret_phrase", [prompt_agent_address], notification_agent_address)
fund_agent_if_low(prompt_agent.wallet.address())

if __name__ == "__main__":
    prompt_agent.run()