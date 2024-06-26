#!/usr/bin/env python
import os
import jwt

from dotenv import load_dotenv

load_dotenv()

DEFAULT_KEY = "547761734272696c6c6967416e64546865536c69746879546f76657344696447797265416e6447696d626c65496e54686557616265416c6c4d696d737957657265546865426f726f676f766573416e645468654d6f6d6552617468734f75746772616265"

secret = bytes.fromhex(os.environ.get("AUTH_SECRET_B16", DEFAULT_KEY))

def issue(whom, tags):
    payload = dict()
    payload['sub'] = whom
    payload['tags'] = tags
    try:
        return jwt.encode(payload, secret, algorithm="HS256")
    except:
        return None

def verify(token):
    res = {}
    try:
        res = jwt.verify(token, secret, ["HS256"])
    except:
        return None
