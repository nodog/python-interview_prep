#

import unittest

from Item import Item


class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item(number=10, description='washer', price=0.02)

    def test_item_number(self):
        self.assertEqual(self.item.number, 10)

    def test_item_description(self):
        self.assertEqual(self.item.description, 'washer')

    def test_item_price(self):
        self.assertAlmostEqual(self.item.price, 0.02, places=2)


if __name__ == '__main__':
    unittest.main()
