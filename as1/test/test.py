from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

crypthos = ["bitcoin", "Ethereum", "Cardano", "Tether", "Binance Coin"]

n = int(input())

for x in range(0,n) :
    print(cg.get_price(crypthos[x], "usd"))



