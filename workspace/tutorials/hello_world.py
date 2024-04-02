import numpy as np

from Pyfhel import Pyfhel


def tutorial_hello_world():
    """
    기본적인 덧셈, 뺄셈, 곱셈 연산에 대한 튜토리얼 함수입니다.

    """
    print("1. Import Pyfhel class, and numpy for the inputs to encrypt.")

    HE = Pyfhel()  # Creating empty Pyfhel object
    HE.contextGen(scheme="bfv", n=2**14, t_bits=20)  # Generate context for 'bfv'/'ckks' scheme
    # The n defines the number of plaintext slots.
    #  There are many configurable parameters on this step
    #  More info in Demo_2, Demo_3, and Pyfhel.contextGen()
    HE.keyGen()  # Key Generation: generates a pair of public/secret keys

    print("2. Context and key setup")
    integer1 = np.array([127], dtype=np.int64)
    integer2 = np.array([-2], dtype=np.int64)
    ctxt1 = HE.encryptInt(integer1)  # Encryption makes use of the public key
    ctxt2 = HE.encryptInt(integer2)  # For integers, encryptInt function is used.

    print("3. Integer Encryption, ")
    print("    int ", integer1, "-> ctxt1 ", type(ctxt1))
    print("    int ", integer2, "-> ctxt2 ", type(ctxt2))

    print(ctxt1)
    print(ctxt2)

    ct_sum = ctxt1 + ctxt2  # `ctxt1 += ctxt2` for inplace operation
    ct_sub = ctxt1 - ctxt2  # `ctxt1 -= ctxt2` for inplace operation
    ct_mul = ctxt1 * ctxt2  # `ctxt1 *= ctxt2` for inplace operation

    print("4. Operating with encrypted integers")
    print(f"Sum: {ct_sum}")
    print(f"Sub: {ct_sub}")
    print(f"Mult:{ct_mul}")

    # Decryption must use the corresponding function
    #  decryptInt.
    res_sum = HE.decryptInt(ct_sum)
    res_sub = HE.decryptInt(ct_sub)
    res_mul = HE.decryptInt(ct_mul)
    print("#. Decrypting result:")
    print("     addition:       decrypt(ctxt1 + ctxt2) =  ", res_sum)
    print("     substraction:   decrypt(ctxt1 - ctxt2) =  ", res_sub)
    print("     multiplication: decrypt(ctxt1 + ctxt2) =  ", res_mul)
