from sys import stdin
count = int(stdin.readline().rstrip())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b #값 교환
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for i in range(count):
    first, sec = map(int,stdin.readline().rstrip().split()) #입력받음
    print(lcm(first, sec))



