from datetime import date
import json
import time
from hashlib import sha256
from urllib.parse import urljoin

import requests
import pyotp


class BxIn():
    def __init__(self, api_key, api_secret, otp=None, url=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.otp = otp
        self.base_url = url or 'https://bx.in.th/api/'

    def get_url(self, url, **kwargs):
        if kwargs:
            url = '{}/?{}'.format(url, '&'.join([f'{k}={v}' for k, v in kwargs.items()]))
        return urljoin(self.base_url, url)

    def get_params(self, **kwargs):
        params = {}
        for key, value in kwargs.items():
            if value != None:
                params[key] = value
        return params

    def get_date(self, date):
        return date and date.strftime('%Y-%m-%d')

    def public(self, url, **kwargs):
        resp = requests.get(self.get_url(url, **kwargs))
        return json.loads(resp.content)

    def private(self, url, data={}):
        nonce = round(time.time())
        m = sha256()
        m.update(f'{self.api_key}{nonce}{self.api_secret}'.encode())
        signature = m.hexdigest()
        if self.otp:
            data['twofa'] = pyotp.TOTP(self.otp).now()
        data['key'] = self.api_key
        data['nonce'] = nonce
        data['signature'] = signature
        resp = requests.post(self.get_url(url), data)
        return json.loads(resp.content)

    def pairing(self):
        return self.public('pairing')

    def orderbook(self, pair=None):
        return self.public('orderbook', **self.get_params(pairing=pair))

    def trade(self, pair=None):
        return self.public('trade', **self.get_params(pairing=pair))

    def tradehistory(self, date, pair=None):
        return self.public('tradehistory', **self.get_params(
            pairing=pair, date=self.get_date(date)))

    def order(self, pairing, amount, rate, buy=True):
        data = {
            'pairing': pairing,
            'amount': amount,
            'rate': rate,
            'type': 'buy' if buy else 'sell',
        }
        return self.private('order', data)

    def cancel(self, pairing, order_id):
        data = {
            'pairing': pairing,
            'order_id': order_id,
        }
        return self.private('cancel', data)

    def balance(self):
        return self.private('balance')

    def getorders(self, pairing, buy=True):
        data = {
            'pairing': pairing,
            'type': 'buy' if buy else 'sell',
        }
        return self.private('getorders', data)

    def history(self, currency, type, start_date=None, end_date=None):
        data = {
            'currency': currency,
            'type': type,
            'start_date': self.get_date(start_date),
            'end_date': self.get_date(end_date),
        }
        return self.private('getorders', data)

    def deposit(self, currency, new=False):
        data = {
            'currency': currency,
            'new': new,
        }
        return self.private('deposit', data)

    def withdrawal(self, currency, amount, address=None, bank_id=None):
        data = {
            'currency': currency,
            'amount': amount,
        }
        if address:
            data['address'] = address
        if bank_id:
            data['bank_id'] = bank_id
        return self.private('withdrawal', data)

    def withdrawal_history(self):
        return self.private('withdrawal-history')
