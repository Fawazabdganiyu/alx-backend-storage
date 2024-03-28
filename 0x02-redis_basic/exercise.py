#!/usr/bin/env python3
""" Definition of Cache module """
import redis
import uuid
from typing import Union


class Cache:
    """ Definition of Cache class """


def __init__(self):
    """ Instantiation """
    self._redis = redis.Redis()
    self._redis.flushdb()


def store(self, data: Union[str, bytes, int, float]) -> str:
    """ Store """
    key = str(uuid.uuid4())
    self._redis.set(key, data)

    return key
