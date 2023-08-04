from typing import List


class Shop:
    def __init__(self, name: str, shop_location: list, products: dict):
        self.name = name
        self.shop_location = shop_location
        self.products = products
