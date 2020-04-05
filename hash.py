import hashlib


def gen(payload: str) -> str:
    sha1 = hashlib.sha1()
    sha1.update(payload.encode('UTF-8'))
    return sha1.hexdigest()
