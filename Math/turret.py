n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5  # 두 원의 거리를 제곱근(원의방정식)
    if distance == 0 and r1 == r2:  # 두 원이 동심원이고 반지름이 같을 때 = 무한대
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때 = 1점에서만남
        print(1)
    elif abs(r1-r2) < distance < (r1+r2):  # 두 원이 서로다른 두 점에서 만날 때 = 2점에서만남
        print(2)
    else:
        print(0)  # 그 외에
