#!/usr/bin/env python3
""" Definition of Cache module """
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """ Get a key from the cache and return in a desired format """
        data = self._redis.get(key)
        if data:
            return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """ Get a key with string value from the cache """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """ Get a key with integer value from the cache """
        return self.get(key, fn=int)
