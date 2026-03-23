from fastapi import APIRouter

from models.response.BaseResponse import BaseResponse

ai_router = APIRouter(prefix="/ai", tags=["AI"])

class AIController:

    @staticmethod
    @ai_router.get("/health", response_model=BaseResponse)
    async def health_check():
        return BaseResponse(success=True, message="AI Controller is healthy!")