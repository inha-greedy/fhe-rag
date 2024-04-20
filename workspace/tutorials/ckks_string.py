import numpy as np
from Pyfhel import Pyfhel

def tutorial_ckks_string():
    print("1. Import Pyfhel class and numpy for inputs")

    HE = Pyfhel()  # Creating empty Pyfhel object
    HE.contextGen(scheme="ckks", n=2**14, scale=2**40, qi_sizes=[60, 30, 30, 30, 60])  # Generate context for 'ckks' scheme
    HE.keyGen()  # Key Generation: generates a pair of public/secret keys
    HE.rotateKeyGen()

    print("2. Context and key setup")

    plaintext_string = "Hello, World!"
    print(f"Original string: {plaintext_string}")

    # Convert string to float encoding
    float_encoding = np.array([float(ord(c)) for c in plaintext_string], dtype=np.float64)
    print(f"Float encoding: {float_encoding}")

    ptxt = HE.encodeFrac(float_encoding)
    encrypted_encoding = HE.encryptPtxt(ptxt) 
    print("3. Encrypted float encoding:")
    print(encrypted_encoding)   






# """
# 임베딩 연산이 어떻게 작동하는지? -> 공부해와라
# -> 평문에 대한 임베딩 / 암호문에 대한 임베딩 결정해야 한다
# """