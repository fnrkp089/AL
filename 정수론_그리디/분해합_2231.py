from sys import stdin
n = int(stdin.readline().rstrip())
number = 0
for i in range(1, n+1): #1부터 입력받은 값 까지         
    splited = list(map(int, str(i)))  #i의 값을 각 자리수로 분해 하여 배열에 저장한 뒤,(123 = 1,2,3)
    answer = i + sum(splited)  #분해합: 자기자신 + 자리수들의 합...   
    if(answer == n):#분해합과 입력받은 값이 같다면...            
        number = i  # number의 값을 해당 값으로 바꾼 후                  
        break    #종료한다.
print(number)
#이거 역시 브루트하게 풀엇다.
