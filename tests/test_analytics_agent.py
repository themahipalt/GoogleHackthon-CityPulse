import asyncio

from citypulse.agents.analytics_agent import AnalyticsAgent


async def main():

    agent = AnalyticsAgent()

    response = await agent.ask(
        "Which ward has the highest complaints?"
    )

    print("\nQuestion")
    print(response.question)

    print("\nGenerated SQL")
    print(response.sql)

    print("\nRows")
    print(response.rows)

    print("\nAI Answer")
    print(response.answer)


if __name__ == "__main__":
    asyncio.run(main())