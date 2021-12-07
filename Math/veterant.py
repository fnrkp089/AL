# -*- coding: utf-8 -*-
def oddFinder(num):
    oddRange = int(num ** (1/2))  # 제곱근
    if num == 1:
        return False  # 1일경우 false
    else:
        for i in range(2, (oddRange+1)):  # 입력받은 num에서...
            if num % i == 0:
                return False
        return True


questionList = list(range(2, 246912))
sorted = []
for i in questionList:
    if oddFinder(i):
        sorted.append(i)


while True:
    n = int(input())
    count = 0
    if (n == 0):
        break
    for i in sorted:
        if n < i <= n * 2:
            count = count + 1
    print(count)
