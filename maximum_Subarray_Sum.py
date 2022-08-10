from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    max_sum = 0
    inter_sum = arr[0]
    if max_sum < inter_sum :
        max_sum = inter_sum
    for i in range(1, n):
        inter_sum += arr[i]
        if arr[i] > inter_sum :
            inter_sum = arr[i]
        if inter_sum > max_sum:
            max_sum = inter_sum
    return max_sum 
