# -*- coding: utf-8 -*-
n = int(input())

for i in range(n):
    height, width, number = map(int, input().split())  # map으로 숫자 변환
    floor = number % height  # 층 넘버
    room = number // height + 1  # 몫, 방 넘버
    if(floor == 0):  # 꼭대기층일경우
        floor = height
        room -= 1
    print(floor * 100 + room)
