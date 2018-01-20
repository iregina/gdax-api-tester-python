import json, hmac, hashlib, time, requests, base64, config
from requests.auth import AuthBase

# Create custom authentication for Exchange
class GdaxAuth(AuthBase):
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

        # using API key for authentication
        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'Application/JSON'
        })
        print request
        print request.headers
        return request

api_url = 'https://api.gdax.com/'
auth = GdaxAuth(config.api_key, config.api_secret, config.passphrase)

# Get accounts
your_accounts = requests.get(api_url + 'accounts', auth=auth)
print ""
print "------------------------------------------------"
print "Hello. Welcome to GDAX API Tester in Python!"
print ""
print "These are the following options:"
print "1) balance -> see your gdax wallet balances"
print "2) id -> see your wallet account ids"
print "3) order -> place an order"
print "------------------------------------------------"
print ""
var = raw_input("Which API call would you like to test?: ")
var = var.upper()
if var == "BALANCE":
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
elif var == "ID":
    print ""
    print "YOUR GDAX WALLET ACCOUNT IDs"
    print "----------------------------"
    print "LTC: " + your_accounts.json()[0]['id']
    print "GBP: " + your_accounts.json()[1]['id']
    print "EUR: " + your_accounts.json()[2]['id']
    print "BTC: " + your_accounts.json()[3]['id']
    print "USD: " + your_accounts.json()[4]['id']
    print "ETH: " + your_accounts.json()[5]['id']
    print "BCH: " + your_accounts.json()[6]['id']
    print ""
elif var == "ORDER":
    product_id = raw_input("Which orderbook which you like to use? (btc-usd / eth-usd / ltc-usd) ")
    order_type = raw_input("Would you like to buy or sell? (buy/sell)")
    size = raw_input("Please input the amount of cryto to " + order_type + "?")
    price = raw_input("Price per cryto: ")
    order = {
    'size': float(size),
    'price': float(price),
    'side': order_type,
    'product_id': product_id,
    }
    print "This is a preview of your order:"
    print order
    order_confirmation = raw_input("Does this look good? (Y/N) ")
    if order_confirmation == "Y":
        print "order confirmed"
        r = requests.post(api_url + 'orders', json=order, auth=auth)
        print r.json()
        print "Done!"
    else:
        print "order not confirmed"
elif var == "TEST":
    order = {
    'size': '0.01',
    'price': '1000.00',
    'side': 'sell',
    'product_id': 'LTC-USD',
    'type': 'limit'
    }
    print requests
    r = requests.post(api_url + 'orders', json=order, auth=auth)
    print r.json()
elif var == "LIST ORDERS":
    r = requests.get(api_url + 'orders')
    print r.json
elif var == "BCH":
    print your_accounts.json()[6]['balance']
elif var == "order":
    print "order up!"
else: 
    print "Sorry, that is not a valid response"





