from sys import stdin
from collections import deque
a, b = map(int, stdin.readline().rstrip().split())
arr = list(range(1, a+1))
answer = []
deq = deque(arr)
while len(deq) > 0:
    for _ in range(b-1):
        deq.append(deq.popleft())
    answer.append(deq.popleft())

print('<' + ', '.join(map(str, answer)) + '>')