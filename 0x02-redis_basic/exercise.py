#!/usr/bin/env python3
""" Definition of Cache module """
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """" Store the history of inputs and outputs of a function """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Store inputs and outputs """
        in_key = method.__qualname__ + ":inputs"
        out_key = method.__qualname__ + ":outputs"

        self._redis.rpush(in_key, str(args))

        outputs = method(self, *args, **kwargs)
        self._redis.rpush(out_key, str(outputs))

        return outputs

    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Count the number of times a method has been called """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Count before returning the called method """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """ Definition of Cache class """

    def __init__(self):
        """ Instantiation """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
