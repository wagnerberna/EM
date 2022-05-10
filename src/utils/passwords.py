from src.utils.response import Response
from src.static.message import *
from bcrypt import hashpw, checkpw, gensalt

response = Response()


def crypt_password(password):
    try:
        salt = gensalt()
        password_hashed = hashpw(password.encode("utf8"), salt)
        return password_hashed
    except Exception as error:

        return response.failed(INTERNAL_ERROR, error), 500


def compare_password(password, password_hashed):
    try:
        if checkpw(password.encode("utf8"), password_hashed.encode("utf8")):
            return True
        return False
    except Exception as error:

        return response.failed(INTERNAL_ERROR, error), 500
