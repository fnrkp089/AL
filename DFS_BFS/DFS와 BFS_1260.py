from sys import stdin
node, line, number = map(int, stdin.readline().rstrip().split())
graph = [[False] * (node + 1) for _ in range(node + 1)] #0은 비워줘야하기때문에 1개 더 생성
destination = [False] * (node + 1) #답 출력용
#print(graph)

for _ in range(line):
  first, second = map(int, stdin.readline().rstrip().split())
  # 노드 연결 하기
  graph[first][second] = graph[second][first] = True #노드와 연결된 그래프 만들기
  #print(graph)
  
def dfs(number):
    destination[number] = True
    print(number, end=' ')
    for i in range(1, node+1):
        if graph[number][i] == True and destination[i] == False:
            dfs(i)
dfs(number)