import json
import uuid

from google import genai

from citypulse.core.config import settings
from citypulse.schemas.complaint import ComplaintReport

client = genai.Client(api_key=settings.GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are generating realistic citizen complaints for Bangalore.

Return ONLY valid JSON.

Schema:

{
    "raw_text":"",
    "image_url":null,
    "latitude":12.9716,
    "longitude":77.5946,
    "ward":"Ward 5"
}

Rules:

- Complaint must sound natural.
- Use different wards.
- Use different wording.
- Categories can include:
    pothole
    garbage
    streetlight
    traffic
- Return ONLY JSON.
"""


async def generate_complaint() -> ComplaintReport:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT,
    )

    text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    print("\n========== GEMINI RAW ==========")
    print(text)
    print("===============================\n")

    data = json.loads(text)

    print(type(data))
    print(data)

    return ComplaintReport(
        report_id=f"SYN-{uuid.uuid4().hex[:8]}",
        **data,
    )