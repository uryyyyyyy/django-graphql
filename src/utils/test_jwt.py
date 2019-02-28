from .jwt import encode, decode


def test_encode_decode():
    token = encode(1)
    _id = decode(token)
    assert _id == 1
