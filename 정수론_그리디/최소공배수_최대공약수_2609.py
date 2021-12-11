from sys import stdin
first, sec = map(int,stdin.readline().rstrip().split()) #입력받음
gcd = 0
def gcd(a, b):
    while b > 0:
        a, b = b, a % b #값 교환
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(first, sec))
print(lcm(first, sec))