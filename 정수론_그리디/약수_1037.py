from sys import stdin
n = int(stdin.readline().rstrip())
el = list(map(int, stdin.readline().rstrip().split()))
el.sort()
print(el[0] * el[-1])