from sys import stdin
parenthesis = int(stdin.readline().rstrip())

for _ in range(parenthesis):
    stack = []
    parenLen=stdin.readline().rstrip()
    for j in parenLen:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) > 0:
                stack.pop()
            else: #스택이 비엇을때
                print("NO")
                break
    else: #for~else문. : break에 걸리지 않앗을때 수행.
        if len(stack) == 0: #else를 걸지 않으면 if else를 한번 더 수행
            print("YES") #break에 걸리지 않앗이게 해당 문을 실행함.
        else:
            print("NO")