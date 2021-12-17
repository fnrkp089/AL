# -*- coding: utf-8 -*-
# dfs를 활용한다

'''
1. 특정 지점의 주변 상 하 좌 우를 살펴보고 주변 지점의 값이 1이면서 아직 방문하지않았다면 해당지점 방문
2. 방문한 지점에서 다시 상 하 좌 우를 살펴 보면서 방문 진행.
3. 모든 노드들에 대해 1~2를 반복하면서 방문하지 않은 지점의 수를 카운트.
'''
from sys import stdin
n = int(stdin.readline().rstrip())
# 2차원 리스트의 맵 정보 입력받기.
graph = []
for i in range(n):
    graph.append(list(map(int, stdin.readline().rstrip().split())))

# 모든 노드에 대해 방문하기.
result = 0


def dfs(x, y):
    # 주어진 범위를 벗어 나는 경우 즉시 종료:
    if(x <= -1 or x >= n or y <= -1 or y >= n):
        return False
        # 현재 노드를 아직 방문하지 않았다면.
    if graph[x][y] == 0:
        # 해당 노드를 방문했다 명시하고
        graph[x][y] = 1
        graph[x-1][y] = 1
        graph[x][y-1] = 1
        graph[x+1][y] = 1
        graph[x][y+1] = 1
        return True
    return False
# 상 하 좌 우의 위치들을 모두 재귀적으로 호출한다.


result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
print(result)
