import hashlib


def sha256(input: str):
    return hashlib.sha256(input.encode("utf-8")).hexdigest()
