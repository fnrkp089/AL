import heapq  # 힙 큐
from sys import stdin
heap = []  # 힙을 위한 배열
n = int(stdin.readline().rstrip())
for _ in range(n):
    i = int(stdin.readline().rstrip())  # 입력값
    if i == 0:  # 0 을 입력받은경우
        if(len(heap) == 0):  # 배열(힙)이 비어있다면 0 출력
            print(0)
        else:
            print((heapq.heappop(heap)))  # 배열안에 값이 존재한다면 해당값 제거
    else:
        heapq.heappush(heap, i)  # 0이 아닐결우 최소힙자료구조로 입력값 저장
