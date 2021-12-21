import itertools  # 중복불가, 순서필요. 즉 Combination


def oddNum(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, (num//2)+1):  # 초기 팀장님 num//2 +1 하면 더 좋다.
            if num % i == 0:
                return False
        return True


def solution(nums):
    count = 0
    arr = []  # 빈배열
    # 콤비네이션으로 3개 뽑기 (어쩌피 다른수이기에 SET필요없음)
    combi = list(itertools.combinations(nums, 3))
    for i in combi:
        if oddNum(sum(i)):       # cmb를 하나씩 가져와 sum한 값을 소수 판별 함수로 넘겨줌
            count += 1
    return count
