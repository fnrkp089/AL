from sys import stdin
from collections import deque
a, b = list(map(int, stdin.readline().rstrip().split()))
eleLen = list(map(int, stdin.readline().rstrip().split()))
arr = list(range(1, a+1))
deq = deque(arr)
count = 0
for i in eleLen:  # 실질적으로 b는 필요없음으로
    while True:
        if list(deq).index(i) == 0:  # 조건에 맞는 데크의 인덱스 0일경우 pop시킨다
            deq.popleft()
            break
        if list(deq).index(i) - 0 < len(list(deq)) - list(deq).index(i):
          # 해당값의 인덱스를 왼쪽, 오른쪽을 비교하여 오른쪽이 더 길다면 popleft시켜 rotate
            deq.append(deq.popleft())
            count += 1
        else:
          # 그외의 경우에는 반대로 rotate
            deq.appendleft(deq.pop())
            count += 1
print(count)
