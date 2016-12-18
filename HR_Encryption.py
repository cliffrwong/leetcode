#!/bin/python3

import sys
import math

s = input().strip()
sLen = len(s)
sqrt = math.sqrt(sLen)

if sqrt.is_integer():
    sqrt = int(sqrt)
    rows, columns = sqrt, sqrt
else:
    sqrt = math.floor(sqrt)
    columns = sqrt+1
    rows = sqrt+1 if sLen > sqrt*(sqrt+1) else sqrt
        
rowed = []
#print(rows, columns)
for j in range(columns):
    for i in range(rows):
        if i*columns+j < sLen:
            rowed.append(s[i*columns+j])
    rowed.append(" ")
result = ''.join(rowed).rstrip()
print(result)
  