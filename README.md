# TITLE

Write a Python code which pulls the data from coingecko.com, and filters out top N cryptocurrencies by market capitalization

## Installation
PyPl
``` bash 
pip install pip install pycoingecko;
```
pandas
``` bash 
pip install pandas;
```

## Usage

``` bash 
from pycoingecko import CoinGeckoAPI
import pprint
import pandas as pd
cg = CoinGeckoAPI()
```

## Examples

``` bash 
C:\Users\Админ\Desktop\ass2>python assignment1coingecko.py
Please define N top of cryptocurrencies
5
TOP 5
1 BTC 796114696123
2 ETH 337362698750
3 USDT 69417385916
4 ADA 68623640483
5 BNB 53551514506

C:\Users\Админ\Desktop\ass2>
```

