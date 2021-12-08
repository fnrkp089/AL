from sys import stdin
n = int(stdin.readline().rstrip())
stack = []
sum = 0
for _ in range(n):
    i = int(stdin.readline().rstrip())
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

for j in stack:
    sum += j

print(sum)
