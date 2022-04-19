# import CoinbasePro which was installed in terminal
import time
import cbpro

# data = stored key phrases
data = open('passphrase', 'r').read().splitlines

public = data[0]
passphrase = data[1]
secret = data[2]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

print(auth_client.get_accounts())

# buy an order for this price in $, size = amount of token, order type = what type of order, product id = token
print(auth_client.buy(price="10.0", size="0.1",
                      order_type="limit", product_id="ETH-USD"))

# buy order no.2
print(auth_client.place_limit_order(
    product_id="BTC-USD", side="buy", price="20.00", size="1"))

# selling
print(auth_client.sell(price="400000000.00", size="10",
      order_type="market", product_id="BTC-USD"))


# cancel order
print(auth_client.cancel_all(product_id="BTC-USD"))

# get orders
print(auth_client=cbpro.AuthenticatedClients(public, secret, passphrase))


# buy/sell based on price; strategy = buy low, sell high

sell_price = 5000000
sell_amount = 5000000

buy_price = 30000000
buy_amount = 300000

while True:
    price = float(auth_client.get_product_ticker(
        product_id="BTC-USD")['price'])
    if price <= buy_price:
        print("Buying Bitcoin")
        auth_client.buy(size=buy_amount, order_type="market",
                        product_id="BTC-USD")
    elif price >= sell_price:
        print("Selling Bitcoin")
        auth_client.sell(size=sell_amount, order_type="market",
                         product_id="BTC-USD")
    else:
        print("No trading happening")
    # how often you'd like it to run
    time.sleep(10)
