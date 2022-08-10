from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    max_price = 0
    min_price = max(prices) +1
    for i in prices:
        min_price = min(i, min_price)
        max_price = max(i-min_price , max_price)
    return max_price
