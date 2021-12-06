# -*- coding: utf-8 -*-
def gcd(x, y, z):
    # 처음 둘중 작은거 구하기
    a = x/y  # 5로 나눈 몫
    b = x/z  # 3으로 나눈 몫

    if(x % y == 0 and (a < z)):
        print(a)
    elif(x % z == 0 and (b < y)):
        print(b)
    else:
        # 나누어 떨어지지 않을때, 둘을 이용해 구하기
        d = x - a*y  # 5로 나눈 값을 빼줌
        if(d == 3):
            e = d/z
            print(e+a)
        elif(d < 3):
            d = d + 5  # 수 변환
            a = a - 1  # 몫 변환
            e = d / z  # 3으로 나누기
            print(e+a)  # 두개의 몫 합치기
        elif(d >= 3 and d < 5):
            e = d/z
            print(e+a+1)
        else:
            print -1


gcd(4999, 5, 3)
