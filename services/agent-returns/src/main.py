from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents.llm_agent import Agent

agent = Agent(
    model="gemini-3-flash-preview",
    name="returns_expert",
    instruction="Strict Policy: Electronics have a 14-day return window and require photo proof of damage.",
)

a2a_app = to_a2a(agent, port=8000)
