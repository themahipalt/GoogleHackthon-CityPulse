import uuid

from google.genai import types

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from citypulse.agent import root_agent


class ChatService:

    def __init__(self):

        self.app_name = "citypulse"

        self.user_id = "default-user"

        self.session_service = InMemorySessionService()

        self.runner = Runner(
            agent=root_agent,
            app_name=self.app_name,
            session_service=self.session_service,
        )

    async def chat(self, message: str) -> str:

        session = await self.session_service.create_session(
            app_name=self.app_name,
            user_id=self.user_id,
            session_id=str(uuid.uuid4()),
        )

        final_answer = ""

        async for event in self.runner.run_async(
            user_id=self.user_id,
            session_id=session.id,
            new_message=types.Content(
                role="user",
                parts=[
                    types.Part(text=message)
                ],
            ),
        ):

            if event.is_final_response():

                final_answer = event.content.parts[0].text

        return final_answer