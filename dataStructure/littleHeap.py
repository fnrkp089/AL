import heapq
from sys import stdin
heap =[]
n = int(stdin.readline().rstrip())
for _ in range(n):
    i = int(stdin.readline().rstrip())
    if i == 0 :
        if( len(heap) == 0 ):
            print(0)
        else:
            print((heapq.heappop(heap)))
    else:
        heapq.heappush(heap, i)
