#!/usr/bin/env python3
""" Doc
"""
import requests


def get_page(url: str) -> str:
    """ Doc """
    r = requests.get(url)
    return r.text
