from app.interfaces.base_price import BasePrice
from app.repositories.product_prices import ProductPricesRepo
from app.repositories.special_prices import SpecialPricesRepo

from collections import Counter


class SpecialProducts(BasePrice):
    def __init__(self):
        self.special_prices = SpecialPricesRepo().get_prices()
        self.product_prices = ProductPricesRepo().get_prices()

    def calculate_price(self, products):
        discount = 0
        product_ctr = Counter(products)
        for product, quantity in product_ctr.items():
            if product not in self.special_prices:
                continue
            special_price = self.special_prices[product]['price']
            special_quantity = self.special_prices[product]['quantity']
            if quantity >= special_quantity:
                disc_quantity = quantity // special_quantity
                discount -= (
                        self.product_prices[product]['price'] * disc_quantity * special_quantity
                        - special_price * disc_quantity
                )
        return discount
