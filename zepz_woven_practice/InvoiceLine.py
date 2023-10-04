#

import math


class InvoiceLine:
    def __init__(self, number, description='', price=0.00, quantity=0):
        self.number = number
        self.description = description
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        if self.number == other.number and \
                self.description == other.description and \
                math.isclose(self.price, other.price, abs_tol=0.001) and \
                self.quantity == other.quantity:
            return True
        else:
            return False
