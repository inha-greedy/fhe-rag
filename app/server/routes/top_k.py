from fastapi import APIRouter
from pydantic import BaseModel

from ..services.top_k import get_top_k


class Query(BaseModel):
    query_message: str


top_k_router = APIRouter()


@top_k_router.post("/top_k")
async def top_k(query: Query):
    """
    top-k를 가져옵니다.
    """
    result = get_top_k(query_message=query.query_message)
    return result
