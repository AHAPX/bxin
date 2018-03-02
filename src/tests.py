import json
from datetime import date
from unittest import TestCase

from bxinth import BxIn

try:
    OTP = None
    from config_test import *
except:
    print('config_test.py not found, please add test api key, secret and otp if required')
    exit()


class BxTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bx = BxIn(API_KEY, API_SECRET, OTP)

    def check_response(self, response):
        self.assertTrue(response.get('success'))
        self.assertIsNone(response.get('error'))

    def test_pairing(self):
        resp = self.bx.pairing()
        self.assertTrue(len(resp) > 1)

    def test_orderbook(self):
        resp = self.bx.orderbook()
        self.assertIn('bids', resp)
        self.assertIn('asks', resp)

    def test_trade(self):
        resp = self.bx.trade()
        self.assertIn('highbid', resp)
        self.assertIn('lowask', resp)
        self.assertIn('trades', resp)
        self.assertIn('user_orders', resp)

    def test_tradehistory(self):
        resp = self.bx.tradehistory(date=date(2018, 1, 1))
        self.assertTrue(resp.get('success'))
        self.assertIn('data', resp)
