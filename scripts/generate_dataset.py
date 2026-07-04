import asyncio

from citypulse.agents.generator_agent import generate_complaint
from citypulse.database.repository import ComplaintRepository
from citypulse.database.init_db import init_db


async def main():

    init_db()

    repository = ComplaintRepository()

    TOTAL_RECORDS = 10
    MAX_RETRIES = 3

    success_count = 0
    failure_count = 0

    for i in range(TOTAL_RECORDS):

        for attempt in range(MAX_RETRIES):

            try:

                complaint = await generate_complaint()

                repository.save_complaint(complaint)

                success_count += 1

                print(
                    f"✅ {success_count}/{TOTAL_RECORDS} "
                    f"{complaint.report_id}"
                )

                # Prevent hitting Gemini rate limits
                await asyncio.sleep(1)

                break

            except Exception as ex:

                print(
                    f"⚠️ Attempt {attempt + 1} failed: {ex}"
                )

                if attempt == MAX_RETRIES - 1:

                    failure_count += 1

                    print(
                        f"❌ Skipping complaint {i + 1}"
                    )

                else:

                    print("🔄 Retrying in 2 seconds...")

                    await asyncio.sleep(2)

    print("\n==============================")
    print("Dataset Generation Complete")
    print("==============================")
    print(f"Generated : {success_count}")
    print(f"Failed    : {failure_count}")
    print("==============================")


if __name__ == "__main__":
    asyncio.run(main())