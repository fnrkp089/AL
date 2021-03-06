# -*- coding: utf-8 -*-
m, n = map(int, input().split())
datas = [True] * (n + 1)

datas[0] = False
datas[1] = False

for i in range(2, (n+1) // 2):
    if datas[i]:  # true
        for j in range(i+i, n+1, i):  # range로 공배수 제거
            datas[j] = False

for i in range(m, n+1):
    if datas[i]:
        print(i)
