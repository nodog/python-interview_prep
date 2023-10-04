#

import unittest

from InvoiceLine import InvoiceLine


class TestInvoiceLine(unittest.TestCase):

    def setUp(self):
        self.invoice_line = InvoiceLine(
            number=10, description='washer', price=0.02, quantity=12)

    def test_invoice_line_number(self):
        self.assertEqual(self.invoice_line.number, 10)

    def test_invoice_line_description(self):
        self.assertEqual(self.invoice_line.description, 'washer')

    def test_invoice_line_price(self):
        self.assertAlmostEqual(self.invoice_line.price, 0.02, places=2)

    def test_invoice_line_quantity(self):
        self.assertEqual(self.invoice_line.quantity, 12)

    def test_invoice_line_equality(self):
        compare_invoice_line_1 = InvoiceLine(
            number=10, description='washer', price=0.02, quantity=12)
        compare_invoice_line_2 = InvoiceLine(
            number=9, description='washer', price=0.02, quantity=12)
        compare_invoice_line_3 = InvoiceLine(
            number=10, description='washet', price=0.02, quantity=12)
        compare_invoice_line_4 = InvoiceLine(
            number=10, description='washer', price=0.03, quantity=12)
        compare_invoice_line_5 = InvoiceLine(
            number=10, description='washer', price=0.02, quantity=13)

        self.assertEqual(self.invoice_line, compare_invoice_line_1)
        self.assertNotEqual(self.invoice_line, compare_invoice_line_2)
        self.assertNotEqual(self.invoice_line, compare_invoice_line_3)
        self.assertNotEqual(self.invoice_line, compare_invoice_line_4)
        self.assertNotEqual(self.invoice_line, compare_invoice_line_5)


if __name__ == '__main__':
    unittest.main()
