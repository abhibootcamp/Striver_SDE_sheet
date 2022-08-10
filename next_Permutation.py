from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    itr = n-2
    itr_plus = n-1
    first_index = -1
    res = []
    while (itr >= 0):
        if permutation[itr] < permutation[itr_plus] :
            first_index = itr
            break
        itr -= 1
        itr_plus -= 1
    if first_index < 0:
        permutation.sort()
        return permutation
    itr = n-1
    second_index = -1
    while (itr >= 0):
        if permutation[itr] > permutation[first_index]:
            second_index = itr
            break
        itr -= 1
    permutation[first_index], permutation[second_index] = permutation[second_index], permutation[first_index]
    from_left = first_index +1
    from_right = n-1
    while from_left < from_right:
        permutation[from_left], permutation[from_right] = permutation[from_right], permutation[from_left]
        from_left += 1
        from_right -= 1
    return permutation
