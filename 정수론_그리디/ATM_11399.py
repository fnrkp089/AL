from sys import stdin
n = int(stdin.readline().rstrip())
timeList = list(map(int,stdin.readline().rstrip().split())) #입력받은 가중치
timeList.sort() #가중치를 sort
count = 0
for i in range(len(timeList) + 1): # i를 돌리되,
    for j in range (i): #각 배열의 번호 이전의 모든 수를 더해서 count에 더해나간다.
        count += timeList[j]
print(count)