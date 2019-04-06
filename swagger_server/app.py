#!/usr/bin/env python3
'''
Basic example of a resource server
'''

import time
import sys,os
sys.path.append(os.getcwd() + '/swagger_server')
from flask_cors import CORS
import connexion
import six
from werkzeug.exceptions import Unauthorized
import logging
from jose import JWTError, jwt

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'change_this'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'
app = connexion.FlaskApp(__name__, specification_dir='swagger/')
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def generate_token(user_id):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(user_id),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def get_secret(user, token_info) -> str:
    return '''
    You are user_id {user} and the secret is 'wbevuec'.
    Decoded token claims: {token_info}.
    '''.format(user=user, token_info=token_info)


def _current_timestamp() -> int:
    return int(time.time())

def say_hello() -> int:
    return int(time.time())

if __name__ == '__main__':
    CORS(app.app)
    app.add_api('openapi.yaml')
    app.run(debug=True)

