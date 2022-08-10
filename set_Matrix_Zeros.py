from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    n = len(matrix)
    m = len(matrix[0])
    first_row_zero = False
    for i in range(m):
        if matrix[0][i] == 0:
            first_row_zero = True
    first_col_zero = False
    for i in range(n):
        if matrix[i][0] == 0:
            first_col_zero = True
    
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, n):
        for j in range(1, m):
            if (matrix[i][0] == 0) or (matrix[0][j] == 0):
                matrix[i][j] = 0

    if first_row_zero :
        for i in range(m):
            matrix[0][i] = 0
    if first_col_zero :
        for i in range(n):
            matrix[i][0] = 0
    return matrix
