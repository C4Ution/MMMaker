import secrets


def random_str():
    return secrets.token_hex(nbytes=16)
