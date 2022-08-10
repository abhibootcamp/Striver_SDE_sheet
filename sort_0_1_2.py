from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
    track_0 = 0
    track_2 = n-1
    i = 0
    while i <= track_2:
        if arr[i] == 0:
            arr[track_0], arr[i] = arr[i], arr[track_0]
            track_0 += 1
            i += 1
            continue
        if arr[i] == 2:
            arr[track_2], arr[i] = arr[i], arr[track_2]
            track_2 -= 1
            continue
        i +=1 
