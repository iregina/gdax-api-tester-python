#import gdax 
#public_client = gdax.PublicClient()

# Requires python-requests. Install with pip:
#
#   pip install requests
#
# or, with easy-install:
#
#   easy_install requests

import json, hmac, hashlib, time, requests, base64, config
from requests.auth import AuthBase

# Create custom authentication for Exchange
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = config.api_key
        self.secret_key = config.api_secret
        self.passphrase = config.passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

api_url = 'https://api.gdax.com/'
auth = CoinbaseExchangeAuth(config.api_key, config.api_secret, config.passphrase)

# Get accounts
your_accounts = requests.get(api_url + 'accounts', auth=auth)

# [{"id": "a1b2c3d4", "balance":...

# Place an order
"""
order = {
    'size': 1.0,
    'price': 1.0,
    'side': 'buy',
    'product_id': 'BTC-USD',
}
r = requests.post(api_url + 'orders', json=order, auth=auth)
print r.json()
"""
# {"id": "0428b97b-bec1-429e-a94c-59992926778d"}


print "Welcome to GDAX API Tester in Python!"
var = raw_input("Which API call would you like to test?: ")
var = var.upper()
if var == "LTC":
    print your_accounts.json()[0]
elif var == "BALANCE":
    print ""
    print "YOUR GDAX WALLET BALANCE"
    print "------------------------"
    print "LTC: " + your_accounts.json()[0]['balance']
    print "GBP: " + your_accounts.json()[1]['balance']
    print "EUR: " + your_accounts.json()[2]['balance']
    print "BTC: " + your_accounts.json()[3]['balance']
    print "USD: " + your_accounts.json()[4]['balance']
    print "ETH: " + your_accounts.json()[5]['balance']
    print "BCH: " + your_accounts.json()[6]['balance']
    print ""
elif var == "EUR":
    print your_accounts.json()[2]['balance']
elif var == "BTC":
    print your_accounts.json()[3]['balance']
elif var == "USD":
    print your_accounts.json()[4]['balance']
elif var == "ETH":
    print your_accounts.json()[5]['balance']
elif var == "BCH":
    print your_accounts.json()[6]['balance']
elif var == "order":
    print "order up!"
else: 
    print "Sorry, that is not a valid response"
