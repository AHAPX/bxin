# Library for bx.in.th

## Description
Python library for bx.in.th api.

## Requirements
- [python 3.6+](https://www.python.org/download/releases/3.6.0/)
- [pyotp](https://github.com/pyotp/pyotp)
- [requests](https://github.com/requests/requests/)

## Installation
```bash
$ pip install bxinth
```

## Usage
```python
from bxinth import BxIn, pairs


bx = BxIn('api_key', 'api_secret', 'otp')
# get orderbook
book = bx.orderbook(pairs.THBBTC)
bids = book['bids']
asks = book['asks']

# make order
order_id = bx.order(pairs.THBBTC, 1, 33000)['order_id']

# cancel order
bx.cancel(pairs.THBBTC, order_id)
```

## Testing
Add src/config_test.py file with
```python
API_KEY = 'api_key'
API_SECRET = 'api_secret'
OTP = 'otp'
```

and run

```bash
$ python -m unittest
```
