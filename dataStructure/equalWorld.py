# -*- coding: utf-8 -*-
from sys import stdin
while True:
    s = stdin.readline().rstrip() #문자열 입력받음
    if s == '.': #바로 닫아버리는 친구 만나면 브레이크
        break
    stack = [] #스택 생성
    flag = True #판별자 생성
    for i in s:
        if i == '(' or i == '[':
            stack.append(i) #닫는괄호들이면 append

        elif i == ')':
            if len(stack) == 0 or stack[-1] == '[': #만약 다음것이(-1) 다른 기호면 판별자 변화
                flag = False
                break
            elif stack[-1] == '(': #같은 기호면 팝핑
                stack.pop()

        elif i == ']':
            if len(stack) == 0 or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if flag == True and len(stack) == 0:
        print('yes')
    else:
        print('no')