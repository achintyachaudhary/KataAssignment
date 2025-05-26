from abc import abstractmethod


class BasePrice:
    @abstractmethod
    def calculate_price(self, products):
        pass
