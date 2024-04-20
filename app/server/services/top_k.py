"""
top-k 호출에 사용하는 비즈니스 로직을 담은 코드 페이지입니다.
"""

import numpy as np

import Pyfhel.Pyfhel
from Pyfhel import Pyfhel, PyCtxt


def get_top_k(context: bytes, pk: bytes, rlk: bytes, rtk: bytes, cx: bytes):
    """
    query message로부터 top-k를 가져와 반환합니다.
    """

    he_server = Pyfhel()
    he_server.from_bytes_context(context)
    he_server.from_bytes_public_key(pk)
    he_server.from_bytes_relin_key(rlk)
    he_server.from_bytes_rotate_key(rtk)

    ctxt = PyCtxt(pyfhel=he_server, bytestring=cx)

    print(f"[Server] received HE_server={he_server} and ctxt={ctxt}")

    # Encode weights in plaintext
    w = np.array([0.5, -1.5, 4, 5])
    ptxt_w = he_server.encode(w)

    # Compute weighted average
    c_mean = ctxt * ptxt_w
    c_mean /= 4  # 4
    c_mean += c_mean >> 1  # cumulative sum
    c_mean += c_mean >> 2  # element [3] contains the result
    print(f"[Server] Average computed! Responding: c_mean={c_mean}")

    # Serialize encrypted result and answer it back
    return c_mean.to_bytes().decode("cp437")
