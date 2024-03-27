#!/usr/bin/env python3
""" Definition of schools_by_topic function """


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of school having a specific topic

    Args:
        mongo_collection (obj): The pymongo collection object
        topic (str): The topic to search for in the collection

    Returns:
        list: A list of documents in the given collection
    """
    result = mongo_collection.find({'topics': {'$in': [topic]}})
    if result:
        return list(result)

    return []
