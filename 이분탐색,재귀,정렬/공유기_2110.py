# -*- coding: utf-8 -*-
from sys import stdin
n, c = map(int, stdin.readline().rstrip().split())
arr = []

for _ in range(n):
    arr.append(int(stdin.readline().rstrip()))
arr.sort()

start = 1  # 시작점
end = arr[-1] - arr[0]  # 좌표차이 계산으로 길이 구하기
answer = 0  # 답


while start <= end:  # 같아질때 까지 반복
    middle = (start + end) // 2  # 중간점
    current = arr[0]  # 배열에 가장 작은값
    count = 1  # 세는용도

    for i in range(1, len(arr)):  # arr를 순회하는데
        if arr[i] >= current + middle:  #
            count += 1
            current = arr[i]

    if count >= c:  # 공유기가 중간점보다 크거나 같을경우
        start = middle + 1  # 시작점 조정
        answer = middle  # 답에 기록
    else:
        end = middle - 1

print(answer)
