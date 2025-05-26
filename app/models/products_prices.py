from app.interfaces.base_price import BasePrice
from app.repositories.product_prices import ProductPricesRepo

from collections import Counter
class ProductPrices(BasePrice):
    def __init__(self):
        self.product_prices = ProductPricesRepo().get_prices()

    def calculate_price(self, products):
        total = 0
        for product in products:
            total += self.product_prices[product]['price']
        return total

