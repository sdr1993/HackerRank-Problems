#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    c=d=0
    for i in range(3):
        if a[i]<b[i]:
            d=d+1
        if a[i]>b[i]:
            c=c+1
        if a[i]==b[i]:
            c=c+0;
            d=d+0;
    return [c,d]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
