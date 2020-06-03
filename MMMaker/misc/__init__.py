import os
import secrets

from conf.settings import BASE_DIR

WORKING_DIR = os.path.join(BASE_DIR, 'temp_files')


def random_str():
    return secrets.token_hex(nbytes=16)


def get_random_name(extension):
    return os.path.join(WORKING_DIR, '{}.{}'.format(random_str(), extension))
