import numpy as np
from Pyfhel import Pyfhel

def tutorial_string_encryption():
    print("1. Import Pyfhel class and numpy for inputs")

    HE = Pyfhel()  # Creating empty Pyfhel object
    HE.contextGen(scheme="ckks", n=2**14, scale=2**40, qi_sizes=[1,2,3,4])  # Generate context for 'ckks' scheme
    HE.keyGen()  # Key Generation: generates a pair of public/secret keys

    print("2. Context and key setup")

    plaintext_string = "Hello, World!"
    print(f"Original string: {plaintext_string}")

    # Convert string to float encoding
    float_encoding = np.array([float(ord(c)) for c in plaintext_string], dtype=np.float64)
    print(f"Float encoding: {float_encoding}")

    # Encrypt float encoding
    encrypted_encoding = HE.encryptFrac(float_encoding)
    print("3. Encrypted float encoding:")
    print(encrypted_encoding)

    # Decrypt encrypted encoding
    decrypted_encoding = HE.decryptFrac(encrypted_encoding)
    print("4. Decrypted float encoding:")
    print(decrypted_encoding)

    # Convert decrypted floats back to string
    decrypted_string = ''.join(chr(int(i)) for i in decrypted_encoding)
    print(f"Decrypted string: {decrypted_string}")


# def string_arithmetic_example():
#     print("1. Import Pyfhel class and numpy for inputs")

#     HE = Pyfhel()  # Creating empty Pyfhel object
#     HE.contextGen(scheme="bfv", n=2**14, t_bits=20)  # Generate context for 'bfv' scheme
#     HE.keyGen()  # Key Generation: generates a pair of public/secret keys

#     print("2. Context and key setup")

#     string1 = "Hello"
#     string2 = "world!"

#     # Convert strings to integer encoding
#     int_encoding1 = np.array([ord(c) for c in string1], dtype=np.int64)
#     int_encoding2 = np.array([ord(c) for c in string2], dtype=np.int64)

#     # Encrypt integer encodings
#     encrypted_encoding1 = HE.encryptInt(int_encoding1)
#     encrypted_encoding2 = HE.encryptInt(int_encoding2)

#     print("3. Encrypted integer encodings:")
#     print(f"String 1: {encrypted_encoding1}")
#     print(f"String 2: {encrypted_encoding2}")

#     # Perform arithmetic operations on encrypted encodings
#     encrypted_sum = encrypted_encoding1 + encrypted_encoding2
#     encrypted_difference = encrypted_encoding1 - encrypted_encoding2
#     encrypted_product = encrypted_encoding1 * encrypted_encoding2

#     # Decrypt results
#     decrypted_sum = HE.decryptInt(encrypted_sum)
#     decrypted_difference = HE.decryptInt(encrypted_difference)
#     decrypted_product = HE.decryptInt(encrypted_product)

#     # Convert decrypted integers back to strings
#     sum_string = ''.join(chr(i) if chr(i).isprintable() else '?' for i in decrypted_sum)
#     difference_string = ''.join(chr(i) if i >= 0 and i < 128 else '?' for i in decrypted_difference)
#     product_string = ''.join(chr(i) if chr(i).isprintable() else '?' for i in decrypted_product)

#     print("4. Results of arithmetic operations on encrypted strings:")
#     print(f"Sum: {sum_string}")
#     print(f"Difference: {difference_string}")
#     print(f"Product: {product_string}")
# """
# 임베딩 연산이 어떻게 작동하는지? -> 공부해와라
# -> 평문에 대한 임베딩 / 암호문에 대한 임베딩 결정해야 한다
# """