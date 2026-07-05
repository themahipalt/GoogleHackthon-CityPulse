from citypulse.agents.analytics_agent import AnalyticsAgent

async def analytics_tool(question: str) -> str:

    analytics = AnalyticsAgent()

    result = await analytics.ask(question)

    return result.answer