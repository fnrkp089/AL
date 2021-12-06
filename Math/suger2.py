n = int(input())
bag = 0
while n >= 0:
    if n % 5 == 0:  # 5의 배수이면
        bag = bag + n // 5  # // = 몫, / = 나누기 끝
        print(bag)
        break
    n = n - 3  # 5의 배수가 가장 크기에 3의 배수로 만들어 줄때까지
    bag = bag + 1  # 3으로 뺴주고 3으로 뺀것은 몫이 되기에 더해준다
else:
    print(-1)
