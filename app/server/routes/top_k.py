from fastapi import APIRouter
from pydantic import BaseModel

from ..services.top_k import get_top_k


class Query(BaseModel):
    context: str
    pk: str
    rlk: str
    rtk: str
    cx: str


top_k_router = APIRouter()


@top_k_router.post("/top_k")
async def top_k(query: Query):
    """
    top-k를 가져옵니다.
    """
    context = query.context.encode("cp437")
    pk = query.pk.encode("cp437")
    rlk = query.rlk.encode("cp437")
    rtk = query.rtk.encode("cp437")
    cx = query.cx.encode("cp437")

    result = get_top_k(context=context, pk=pk, rlk=rlk, rtk=rtk, cx=cx)
    return result
