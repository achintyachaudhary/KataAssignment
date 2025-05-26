import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    DEBUG = False
    PRODUCT_PRICE_PATH = APP_DIR + "/data/product_prices.json"
    SPECIAL_PRICE_PATH = APP_DIR + "/data/special_prices.json"
