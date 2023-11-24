import hashlib


def create_short_url(full_url: str):
    hash_object = hashlib.md5(full_url.encode())
    hex_hash = hash_object.hexdigest()[:4]
    return hex_hash
