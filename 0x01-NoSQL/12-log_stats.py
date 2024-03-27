#!/usr/bin/env python3
""" A script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient
from pprint import pprint as pp

client = MongoClient()
nginx = client.logs.nginx
# pp(list(nginx.find(limit=3)))
print(f'{nginx.count_documents({})} logs')
print('Methods:')

methods = {
    'GET': nginx.count_documents({'method': 'GET'}),
    'POST': nginx.count_documents({'method': 'POST'}),
    'PUT': nginx.count_documents({'method': 'PUT'}),
    'PATCH': nginx.count_documents({'method': 'PATCH'}),
    'DELETE': nginx.count_documents({'method': 'DELETE'})
}
for method, count in methods.items():
    print(f'    method {method}: {count}')

print(f"{nginx.count_documents({'path': '/status'})} status check")
