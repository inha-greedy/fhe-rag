from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .routes.top_k import top_k_router
from .routes.upload import upload_router
from .services.session import set_user_id


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(top_k_router)


@app.middleware("http")
async def add_user_id_to_request(request: Request, call_next):
    """
    모든 요청에 대해 사용자 ID를 추가합니다.
    """
    set_user_id(request)
    response = await call_next(request)
    return response
