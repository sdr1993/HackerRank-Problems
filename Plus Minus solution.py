#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the plusMinus function below.
def plusMinus(arr):
    p=ne=z=0
    for i in arr:
        if i>0:
            p=p+1
        if i<0:
            ne=ne+1
        if i==0:
            z=z+1
    print(str.format('{0:.6f}',float(p/n)))
    print(str.format('{0:.6f}',float(ne/n)))
    print(str.format('{0:.6f}',float(z/n))) 
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)