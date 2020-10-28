import json
from typing import re


def read_data(path="data/data.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def get_product_byid(product_id):
    products = read_data(path='data/products.json')
    for p in products:
        if p["id"] == get_product_byid:
            return p

