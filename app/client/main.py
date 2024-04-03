from dotenv import load_dotenv

from .services.query import query_message
from .tutorials.hello_world import tutorial_hello_world


def main():
    """
    실행할 메인 함수입니다.
    """

    # 1. llm request and response
    load_dotenv()
    message_input = "hello world!"
    answer = query_message(message_input=message_input)
    print(f"{answer=}")

    # 2. pyfhel example
    tutorial_hello_world()


if __name__ == "__main__":
    main()
