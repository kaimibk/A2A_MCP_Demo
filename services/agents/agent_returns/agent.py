from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(
        model="openai/nemotron-3-nano:4b",
        api_key="ollama",
        api_base="http://host.docker.internal:11434/v1",
    ),
    name="returns_expert",
    instruction="Strict Policy: Electronics have a 14-day return window and require photo proof of damage.",
)

a2a_app = to_a2a(root_agent, host="0.0.0.0", port=8000)
