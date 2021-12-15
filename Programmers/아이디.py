from sys import stdin


def solution(new_id):
    answer = ''
    # Step 1 소문자 치환:
    lowId = new_id.lower()

    # Step 2 알파벳, 숫자, 특수문자:
    for i in lowId:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i

    # Step 3 점두개 점 하나로:
    while '..' in answer:
        answer = answer.replace('..', '.')

    # Step 4:
    if(answer[0] == '.' or answer[-1] == '.'):
        answer.strip('.')

    # Step 5:
    if answer == '':
        answer = 'a'

    # Step 6:
    if len(answer) >= 16:
        answer = answer[:15].rstrip(".")

    # Step 7:
    if len(answer) <= 2:
        pluser = answer[-1]
        while len(answer) < 3:
            answer += pluser

    return answer


n = stdin.readline().rstrip()
