# -*- coding: utf-8 -*-
#a, b, c = map(int, input().split())
#
#count = 0
#while( c >= 0 ):
#    c = c - a
#    c = c + b
#    count += 1
#print(count) BRUTE!!!!!!!!

import sys
import math
a, b, c = map(int, input().split())

count = 0
count = (c - b) / (a - b)
print(math.ceil(count))