"""
세션 설정에 사용되는 비즈니스 로직을 담은 코드 페이지입니다.
"""

from fastapi import Request


user_map = {"sequence": 1000}


def get_user_id() -> int:
    """
    get user_id
    """
    try:
        return user_map["user_id"]

    except KeyError:
        return 999


def set_user_id(request: Request):
    """
    set user_id
    """
    origin = request.headers.get("origin")
    agent = request.headers.get("user-agent")
    user_key = f"origin:{origin}::agent:{agent}"

    if user_key not in user_map:
        # sequence를 가져와 업데이트합니다
        user_map["sequence"] = user_map["sequence"] + 1

        # 가져온 sequence를 이용해 새 user를 등록합니다
        user_map[user_key] = user_map["sequence"]

    user_map["user_id"] = user_map[user_key]
