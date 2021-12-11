'''
조합문제
동쪽(east)에 다리(bridge)를 놓을수 있는 경우의 수
mCn = m! / (m-n)! * n! 
단 /를 사용할시 float되기에 //로

'''
from sys import stdin
howMany = int(stdin.readline().rstrip())
def factorial(n): #팩토리얼 함수
    num = 1
    for i in range(1, n+1): # 3: 1*2*3
        num = num*i
    return num
        
for _ in range(howMany):
    bridge, eastSite = map(int, stdin.readline().rstrip().split())
    count = factorial(eastSite) // (factorial(eastSite - bridge) * factorial(bridge))
    print(count)
    
