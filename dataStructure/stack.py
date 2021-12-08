# -*- coding: utf-8 -*-
from sys import stdin

n = int(input())
arr = []
for _ in range(n):
    order = stdin.readline().rstrip().split()
    if(order[0] == 'push'):
        arr.append(int(order[1]))
    elif(order[0] == 'pop'):
        if(len(arr) < 1):
            print(-1)
        else:
            a = arr.pop()
            print(a)
    elif(order[0] == 'size'):
        print(len(arr))

    elif(order[0] == 'empty'):
        arrLen = len(arr)
        if(arrLen > 0):
            print(0)
        else:
            print(1)
    else:  # top
        if(len(arr) < 1):
            print(-1)
        else:
            print(arr[len(arr)-1])
