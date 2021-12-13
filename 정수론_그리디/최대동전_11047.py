from sys import stdin
howMany, money = map(int, stdin.readline().rstrip().split())
arr = []
for _ in range(howMany):
    n = int(stdin.readline().rstrip())
    arr.append(n)
arr.reverse() # 큰수부터 계산
count = 0
for i in arr: #arr를 순회
    if(money % i >= 0): #나머지가 클경우
        count = count + (money // i) #count에 몫을 더하고
        money = money % i #money는 값의 나머지이다
    if(money == 0): #만일 돈이 0이됫을경우
        print(count) #해당 count를 출력
        break
