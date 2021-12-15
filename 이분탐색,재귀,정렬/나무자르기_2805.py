# -*- coding: utf-8 -*-
from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
trees = list(map(int, stdin.readline().rstrip().split()))
start, end = 0, max(trees)  # 시작과 끝.

while start <= end:
    mid = (start+end)//2
    tree = 0  # 잘린 나무 합
    for i in trees:
        if i > mid:  # mid보다 큰 나무 높이는 잘림
            tree += i - mid

    if tree >= m:  # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else:  # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1
print(end)
