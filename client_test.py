import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        for quote in quotes:
            bid_price = quote["top_bid"]["price"]
            ask_price = quote["top_ask"]["price"]
            self.assertEqual(
                getDataPoint(quote),
                (quote["stock"], bid_price, ask_price, (bid_price + ask_price) / 2),
            )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        for quote in quotes:
            bid_price = quote["top_bid"]["price"]
            ask_price = quote["top_ask"]["price"]
            self.assertEqual(
                getDataPoint(quote),
                (quote["stock"], bid_price, ask_price, (bid_price + ask_price) / 2),
            )

    def test_getRatio(self):
        price_a = 121.68
        price_b = 119.2
        self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

    def test_getRatio_priceAZero(self):
        price_a = 0
        price_b = 119.2
        self.assertEqual(getRatio(price_a, price_b), 0)

    def test_getRatio_priceBZero(self):
        price_a = 121.68
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b))


if __name__ == "__main__":
    unittest.main()
