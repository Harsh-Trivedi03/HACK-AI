# user_agent.py
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

class UserAgent(Agent):
    def __init__(self, name, seed, endpoint, prompt_agent_address):
        super().__init__(name=name, seed=seed, endpoint=endpoint)
        self.prompt_agent_address = prompt_agent_address

    @Agent.on_event("startup")
    async def startup_behavior(self, ctx: Context):
        # Fetch user requirements (this can be adapted as per actual data collection logic)
        requirements = {
            'position': 'web developer',
            'tech_stacks': ['React', 'NodeJS'],
            'experience': 3
        }
        # Send these requirements to the prompt agent
        await ctx.send(self.prompt_agent_address, requirements)

# Initialize and run the User Agent
user_agent_address = "http://127.0.0.1:8000/submit"  # This should be unique for each agent
prompt_agent_address = "prompt_agent_address_here"  # Address of the Prompt Agent
resume_agent = UserAgent("resume_agent", "user_secret_phrase", [user_agent_address], prompt_agent_address)
fund_agent_if_low(user_agent.wallet.address())

if __name__ == "__main__":
    resume_agent.run()
