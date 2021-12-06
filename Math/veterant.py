# -*- coding: utf-8 -*-
def veterang(m,n):
    m = int(m)
    n = int(n)
    count = 0
    datas = [True] * (n + 1)

    datas[0] = False
    datas[1] = False

    for i in range(2, (n+1)):
        if datas[i]:  # true
            for j in range(i+i, n+1, i):  # range로 공배수 제거
                datas[j] = False # false로 출력

    for i in range(m, n+1):
        if datas[i]:
           count = count +1
    print(count)

call = int(input())
veterang(call, call*2)