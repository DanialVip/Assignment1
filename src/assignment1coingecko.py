from pycoingecko import CoinGeckoAPI
import pprint
import pandas as pd
cg = CoinGeckoAPI()

class Coin:
    def __init__(self, top, name, market_cap):
        self.top = top
        self.name = name
        self.market_cap = market_cap

print("Please define N top of cryptocurrencies")
topN = input()
market = cg.get_coins_markets(vs_currency="usd")

market = sorted(market, key=lambda k: k['market_cap'], reverse=True)
print(f"TOP {topN}")

top = 1
listOfTops = []
for crypto in market:
    name = crypto['symbol'].upper()
    market_cap = crypto['market_cap']
    coin = Coin(top, name, market_cap)
    listOfTops.append(coin)
    top += 1
    if top > int(topN):
        break

for i in listOfTops:
    print(f"{i.top} {i.name} {i.market_cap}")



