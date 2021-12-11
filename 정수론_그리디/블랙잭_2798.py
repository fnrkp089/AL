'''
17분,
순열 조합문제
라이브러리 몰라서 일단 3중 반복문으로 브루트하게 해결
'''
from sys import stdin
a, b = map(int,stdin.readline().rstrip().split())
el = list(map(int, stdin.readline().rstrip().split()))
answer = 0
for i in range(a): #첫번째 수기준으로 다음수, 그다음수를 더하고
    for j in range(i+1, a): #두번째 수 기준으로 세번째 수를 더하고
        for k in range(j+1, a): #세번째 수를 합치되,
            if(el[i] + el[j] + el[k] > b) : #이 세개의 합이 기준치보다 넘을경우
                continue #수를 담지 않고 다음 계산을 한다
            else:
                answer = max(answer, el[i] + el[j] + el[k]) #만일 넘지 않을경우 max로 근접한값(큰값)을 담는다
print(answer)