import asyncio

from citypulse.agents.recommendation_agent import RecommendationAgent


async def main():

    agent = RecommendationAgent()

    result = await agent.recommend()

    print()

    print("=" * 50)
    print("Recommendation")
    print("=" * 50)

    print(result.summary)

    print()

    print(result.recommendation)

    print()

    print(result.confidence)


if __name__ == "__main__":
    asyncio.run(main())