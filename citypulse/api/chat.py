from fastapi import APIRouter
from pydantic import BaseModel

from citypulse.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

service = ChatService()


class ChatRequest(BaseModel):

    message: str


class ChatResponse(BaseModel):

    answer: str


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):

    answer = await service.chat(request.message)

    return ChatResponse(
        answer=answer,
    )