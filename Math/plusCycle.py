n = int(input())


if(n < 10):
    n = n*10 + n

sum = 0
arranger = 0
arranger = n
count = 0
condition = True
while condition == True:
    ten = arranger // 10
    one = arranger % 10
    sum = ten + one
    arranger = one*10 + sum % 10
    count = count + 1
    if(arranger == n):
        condition = False

print(count)
