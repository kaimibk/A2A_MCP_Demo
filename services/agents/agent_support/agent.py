from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import (
    AGENT_CARD_WELL_KNOWN_PATH,
    RemoteA2aAgent,
)
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from google.genai import types

# Consume the pre-made MCP
order_tools = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://host.docker.internal:8000/mcp"
    )
)

# Consume returns A2A
remote_returns = RemoteA2aAgent(
    name="returns_expert",
    description="Handles company return policies.",
    agent_card=f"http://host.docker.internal:8002{AGENT_CARD_WELL_KNOWN_PATH}",
    use_legacy=False,
)

root_agent = Agent(
    model=LiteLlm(
        model="openai/nemotron-3-nano:4b",
        api_key="ollama",
        api_base="http://host.docker.internal:11434/v1",
    ),
    name="support_desk",
    instruction="""
        You are a helpful customer support assistant. Check orders using your tools, and delegate policy questions to the returns expert agent.
        Follow these steps:
            1. When you are asked about an order, use the get_order tool.
            2. When you are asked about returning an item. First call the get_order function for more information about the order, then pass the result to the returns_expert agent so we strictly follow our returns policies.
            3. If you need to verify todays date, use the today_datetime tool. Then you can recall the returns_expert.
        Always clarify the results before proceeding.
    """,
    tools=[order_tools],
    sub_agents=[remote_returns],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            )
        ]
    ),
)

# a2a_app = to_a2a(root_agent, port=8000)
