from app.models.products_prices import ProductPrices
from app.models.special_products import SpecialProducts
from app.processor.product_prices import ProductPriceProcessor


def calculate_product_price(products):
    adjustments = [
        ProductPrices(),
        SpecialProducts()
    ]

    processor = ProductPriceProcessor(adjustments)
    return processor.process(products)
