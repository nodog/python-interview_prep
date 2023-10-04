import unittest
import datetime
from Invoice import Invoice
from InvoiceLine import InvoiceLine


class TestInvoice(unittest.TestCase):

    def setUp(self):
        invoice_lines = [InvoiceLine(10, 'washer', 0.02, 12),
                         InvoiceLine(11, 'bolt', 0.03, 12),
                         InvoiceLine(12, 'wingnut', 0.16, 12)]
        self.invoice = Invoice(
            invoice_number=134, date=datetime.date.today(), lines=invoice_lines)

    def test_invoice_number(self):
        self.assertEqual(self.invoice.invoice_number, 134)

    def test_default_label(self):
        self.assertEqual(self.invoice.default_label(),
                         'make invoice')

    def test_invoice_date(self):
        self.assertEqual(self.invoice.date, datetime.date.today())
        self.assertNotEqual(self.invoice.date, datetime.date(1978, 9, 5))

    def test_invoice_total(self):
        self.assertAlmostEqual(self.invoice.total, 0.00, places=2)

    def test_invoice_lines(self):

        compare_invoice_lines = [InvoiceLine(10, 'washer', 0.02, 12),
                                 InvoiceLine(11, 'bolt', 0.03, 12),
                                 InvoiceLine(12, 'wingnut', 0.16, 12)]
        invoice_lines = self.invoice.lines

        self.assertEqual(self.invoice.lines, invoice_lines)

    def test_invoice_total(self):
        self.assertAlmostEqual(self.invoice.calculate_total(), 2.52, places=2)


if __name__ == '__main__':
    unittest.main()
