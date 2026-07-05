from citypulse.agents.recommendation_agent import RecommendationAgent

recommendation = RecommendationAgent()


async def recommendation_tool() -> str:
    """
    Generates AI recommendations.
    """

    result = await recommendation.recommend()

    return f"""
Summary:
{result.summary}

Recommendation:
{result.recommendation}
"""