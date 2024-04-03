"""
POST /generate
에 사용되는 비즈니스 로직을 담은 코드 페이지입니다.
"""

import logging

from langchain_openai.chat_models.base import ChatOpenAI


def query_message(message_input: str) -> str:
    """
    LLM에 질문을 전달해 답변을 생성합니다.
    """
    logging.info("요청한 질문: %s", message_input)

    llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

    llm_response = llm.invoke(message_input)
    message_output = llm_response.content

    logging.info("생성한 응답: %s", message_output)

    return message_output
