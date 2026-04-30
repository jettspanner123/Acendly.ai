from fastapi import APIRouter
from models.response.BaseResponse import BaseResponse

AI_ROUTER = APIRouter(prefix="/ai", tags=["AI"])

class AIController:

    @staticmethod
    @AI_ROUTER.get("/health", response_model=BaseResponse)
    async def health_check():
        return BaseResponse(success=True, message="AI Controller is healthy!")