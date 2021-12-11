from sys import stdin
import heapq  # 힙 큐
lostPer = stdin.readline().rstrip()
innerArr = []
minus = lostPer.split('-')# - 계산인 친구들로만 묶어준다

#print(minus) #최소가 되려면 마이너스로 기준 괄호로 만든다.

for i in minus:
    sum = 0 #값을 계산할 임시변수
    plus = i.split('+') #현재 i중 +가 존재할 시 나눈다.
    for j in plus:
        sum += int(j) # +값들을 더한다.
    innerArr.append(sum) #답을 계산을 배열안에 해당 값을 넣고,
answer = innerArr[0] #시작값을 넣는다.
    
for i in range(1, len(innerArr)): #시작값이 이미 있기 때문에 innerArr의 갯수만큼 돌되,
    answer -= innerArr[i] #innerArr들을 빼나가면 최소값이 나온다
print(answer)