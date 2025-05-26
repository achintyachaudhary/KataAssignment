from app import Config
from app.utils.file_reader import read_json


class ProductPricesRepo:
    def __init__(self):
        self.p_price = read_json(Config.PRODUCT_PRICE_PATH)

    def get_prices(self):
        return self.p_price
