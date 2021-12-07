n = int(input())

for _ in range(n):
    start, end = map(int, input().split())
    distance = end - start

    dis = 0
    count = 0
    hana = 1

    while dis < distance:
        # 2번 반복해줌
        for _ in range(2):
            before_dis = dis
            count += 1
            dis += hana
            if distance <= dis and distance > before_dis:
                print(count)
        hana += 1
