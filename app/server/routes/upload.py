from fastapi import APIRouter, Form, UploadFile

from ..services.upload import upload_file


upload_router = APIRouter()


@upload_router.post("/upload")
async def upload(file: UploadFile = Form(...)):
    """
    암호화된 파일을 업로드합니다.
    """

    contents = await file.read()
    filename = file.filename.replace(" ", "-")

    return upload_file(contents, filename)
