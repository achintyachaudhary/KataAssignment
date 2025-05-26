from app import Config
from app.utils.file_reader import read_json


class SpecialPricesRepo:
    def __init__(self):
        self.s_price = read_json(Config.SPECIAL_PRICE_PATH)

    def get_prices(self):
        return self.s_price
