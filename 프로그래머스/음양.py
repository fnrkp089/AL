def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        if(signs[i] == False):
            absolutes[i] *= -1
        total += absolutes[i]
    return total
