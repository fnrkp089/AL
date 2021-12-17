# -*- coding: utf-8 -*-
from sys import stdin
n, m, v = map(int, stdin.readline().rstrip().split())
'''
행렬을 만들어주자. 다만 0번 인덱스부터 시작할경우 추가 조정이 필요하기에, 1번 인덱스부터 시작.
'''
matrix = [[0] * (n+1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    matrix[a][b] = matrix[b][a] = 1

# 방문 노드들 확인
visited = [0] * (n+1)


def dfs(v):
    # 들어온 노드는 방문한 노드이기에 해당 노드의 상태를 1로 만들어 방문햇음을 기록
    # 즉 현재 노드를 방문처리.
    visited[v] = 1
    print(v, end='')
    for i in range(1, n+1):
        # 현재 노드와 연결된 다른 노드들을 재귀적으로 방문하자.
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]  # 들려야할 노드 저장.
    visited[v] = 1

    while queue:
        v = queue.pop(0)
        print(v, end='')
        for i in range(1, n+1):
            if visited[i] == 0 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = 1


dfs(v)
visited = [0] * (n+1)
bfs(v)
