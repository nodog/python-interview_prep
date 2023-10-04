#

import Invoice


def generate_invoices(invoice_number_list):

    invoices = []
    for invoice_number in invoice_number_list:
        invoice = Invoice.Invoice(invoice_number)
        print(f'invoice.invoice_number = {invoice.invoice_number}')


if __name__ == '__main__':
    invoice_number_list = [100, 101, 102]
    invoice_run = generate_invoices(invoice_number_list)
    print(invoice_run)
