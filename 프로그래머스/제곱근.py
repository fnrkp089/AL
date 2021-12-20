def solution(n):
    squard = n ** (1/2)
    if squard % 1 == 0:
        return (squard+1) ** 2
    return -1
