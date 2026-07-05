from google.adk.agents import Agent

from citypulse.tools.analytics_tool import analytics_tool
from citypulse.tools.forecast_tool import forecast_tool
from citypulse.tools.recommendation_tool import recommendation_tool
from citypulse.tools.triage_tool import triage_tool

root_agent = Agent(
    name="CityPulse",

    model="gemini-2.5-flash",

    description="AI Decision Intelligence Platform for Smart Cities.",

    instruction="""
You are CityPulse.

Help city officials analyze complaints.

Choose the correct tool.

Use:

analytics_tool

forecast_tool

recommendation_tool

triage_tool

Do not invent data.
""",

    tools=[
        analytics_tool,
        forecast_tool,
        recommendation_tool,
        triage_tool,
    ],
)