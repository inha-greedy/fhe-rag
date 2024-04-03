"""
POST /upload
에 사용되는 비즈니스 로직을 담은 코드 페이지입니다.
"""

import os

from .session import get_user_id


def upload_file(contents: bytes, filename: str) -> dict:
    """
    클라이언트로부터 전달받은 파일을 웹 서버에 저장합니다
    """

    # 저장소를 초기화하고 파일을 저장합니다.
    clear_storage()
    save_file(contents, filename)

    return {"filename": filename}


def get_storage_path() -> str:
    """
    사용자의 저장소 경로를 가져옵니다.
    """
    user_id = get_user_id()
    storage_path = os.path.join("./app/server/storage", str(user_id))
    return storage_path


def _get_subdirectory_path(subdirectory_name: str) -> str:
    """
    사용자의 서브 디렉토리 경로를 가져옵니다.
    """
    storage_path = get_storage_path()
    return os.path.join(storage_path, subdirectory_name)


def get_vectorstore_path() -> str:
    """
    벡터스토어 경로를 가져옵니다.
    """
    return _get_subdirectory_path("vectorstore")


def clear_storage() -> None:
    """
    저장소를 비웁니다.
    """
    storage_path = get_storage_path()
    vectorstore_path = get_vectorstore_path()

    # 기존 디렉토리 및 하위 내용 삭제
    if os.path.exists(storage_path):
        for root, dirs, files in os.walk(storage_path, topdown=False):
            for file_name in files:
                os.remove(os.path.join(root, file_name))
            for dir_name in dirs:
                os.rmdir(os.path.join(root, dir_name))
        os.rmdir(storage_path)

    #  디렉토리 재생성
    os.makedirs(storage_path)
    os.makedirs(vectorstore_path)


def save_file(contents: bytes, filename: str) -> None:
    """
    파일을 확장자에 맞추어 저장합니다.
    """

    save_path = get_vectorstore_path()
    file_path = os.path.join(save_path, filename)

    with open(file_path, "wb") as fp:
        fp.write(contents)
