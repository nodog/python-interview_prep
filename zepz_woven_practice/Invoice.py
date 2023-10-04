#

import datetime


class Invoice:
    def __init__(self, invoice_number, date=datetime.date.today(), lines={}):
        self.invoice_number = invoice_number
        self.date = date
        self.lines = lines
        self.total = 0.00

    def default_label(self):
        return 'make invoice'

    def calculate_total(self):
        total = 0.00
        for line in self.lines:
            total += line.price * line.quantity

        self.total = total
        return self.total


if __name__ == '__main__':
    invoice = Invoice()
    print(invoice.default_label())
