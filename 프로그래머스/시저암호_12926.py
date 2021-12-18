# -*- coding: utf-8 -*-
def solution(s, n):
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in s:  # 입력받은 배열 순회
        if i in big:  # 현재 문자가 대문자일경우
            idx = big.find(i) + n  # 해당 인덱스에서 +n 만큼 더해준 index 만들고
            if(idx <= 25):
                answer += big[idx]  # 해당 인덱스값을 넣어준다.
            else:
                answer += big[idx % 26]  # 초과될시 그만큼 배열의 수에 넣어줘야하기에
        elif i in small:
            idx = small.find(i) + n
            if(idx <= 25):
                answer += small[idx]
            else:
                answer += small[idx % 26]  # 초과될시 그만큼 배열의 수에 넣어줘야하기에
        else:
            answer += ' '  # 공백이면 공백넣어주기
    return answer
