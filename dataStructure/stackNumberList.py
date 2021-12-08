from sys import stdin
n = int(stdin.readline().rstrip())
mine = []
target = []
count = 1
maker = True

for _ in range(n):
    num = int(stdin.readline().rstrip())
    while count <= num:
        mine.append(count)
        target.append('+')
        count += 1
    if mine[-1] == num:
        mine.pop()
        target.append('-')
    else:
        maker = False
if maker == False:
    print('NO')
else:
    for i in target:
        print(i)
