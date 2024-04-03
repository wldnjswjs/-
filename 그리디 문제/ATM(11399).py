n = int(input())                            # 사람수
peoples = list(map(int, input().split()))   # 인당 걸리는 시간
answer = 0                                  # 필요한 시간의 합

peoples.sort()                              # 오름차순 정렬

for i in range(1, n+1):
    answer += sum(peoples[0:i])             # 리스트에서 0부터 i까지의 합을 반복해서 더한다

print(answer)