class ProductPriceProcessor:
    def __init__(self, adjustments):
        self.adjustments = adjustments

    def process(self, products):
        final_amount = 0
        for adjustment in self.adjustments:
            final_amount += adjustment.calculate_price(products)
        return final_amount
