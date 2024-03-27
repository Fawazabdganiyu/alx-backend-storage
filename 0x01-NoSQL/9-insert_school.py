#!/usr/bin/env python3
"""Definition of insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    new = mongo_collection.insert_one(kwargs)
    if new:
        return new.inserted_id
