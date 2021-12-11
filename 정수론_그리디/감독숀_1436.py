from sys import stdin
n = int(stdin.readline().rstrip())
demon = 666
count = 0
while True:
    if '666' in str(demon): # 666이라는 놈이  demon에 존재한다면
        count += 1 #count를 1 증가시킨다.
        
    if count == n: #주어진 수와 count가 같을경우
        print(demon) #demon을 출력하고
        break #종료하되
    
    demon +=1 #count가 같지않을경우 667, 668 ,669.....

    
    