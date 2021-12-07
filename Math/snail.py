# -*- coding: utf-8 -*-

# a, b, c = map(int, input().split())

# count = 0
# while( c >= 0 ):
#    c = c - a
#    print(count)
#    c = c + b
#    print(count)
#    count += 1
# print(count) #BRUTE!!!!!!!!


# a, b, c = map(int, input().split())

# count = 0
# count = (c - b) / (a - b)  # (전체길이 - 내려간양) / (올라갈수 있는 양 - 내려간양) = 실질적으로 올라가는양
# if(type(count) is float and count != 0 and count > 0):
#     count = int(count) + 1
# print(count)

import sys
import math
a, b, c = map(int, input().split())

count = 0
count = (c - b) / (a - b)  # 전체 길이에서 낮에 올라갈수잇는 길이를 빼되, 소수점이잇다면 +1
print(math.ceil(count))  # 소수점이 있으면 +1
