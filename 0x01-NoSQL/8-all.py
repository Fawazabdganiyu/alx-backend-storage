#!/usr/bin/env python3
"""Definition of list_all function
"""


def list_all(mongo_collection):
    """List all documents in a collection
    """
    result = mongo_collection.find()
    if result:
        return list(result)

    return []
