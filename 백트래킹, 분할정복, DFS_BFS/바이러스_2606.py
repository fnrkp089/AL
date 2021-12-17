# -*- coding: utf-8 -*-
from sys import stdin
n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())


matrix = [[0] * (n+1) for i in range(n+1)]
visitied = [0] * (n+1)

for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    # 인접 행렬로 간선을 저장한다...
    matrix[a][b] = matrix[b][a] = 1
    '''
    인접 리스트로 간접을 저장할 경우
    for i in range(1,n+1):
      graph[i] = set()
      
    for _ in range(m):
      a, b = map(int, input().split())
      graph[a].add(b)
      graph[b].add(a)
    '''

result = []


def dfs(v):
    visitied[v] = 1
    for i in range(1, n+1):
        if matrix[v][i] == 1 and visitied[i] == 0:
            result.append(i)
            dfs(i)
    return len(result)


print(dfs(1))
# https://codesyun.tistory.com/276?category=1009697
