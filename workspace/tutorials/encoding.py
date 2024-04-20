def lorem():
    str_A = 'Hello'
    str_B = 'world!'

    # 문자열 인코딩
    encoded_A = [ord(char) for char in str_A]
    encoded_B = [ord(char) for char in str_B]

    print(f"{encoded_A=}")
    print(f"{encoded_B=}")
    
    # 인코딩된 문자열 간 덧셈
    encoded_sum = encoded_A + encoded_B

    print(f"{encoded_sum=}")

    # 출력: [72, 101, 108, 108, 111, 119, 111, 114, 108, 100, 33]

    # 인코딩된 문자열 디코딩
    decoded_str = ''.join(chr(num) for num in encoded_sum)
    print(f"{decoded_str=}")

    # 출력: "Hello world!"
