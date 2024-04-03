n = int(input()) # 도시의 개수
distances = list(map(int,input().split()))  # 도로의 길이
coasts = list(map(int,input().split()))    # 가격

minCoast = coasts[0]    # 최소 비용을 저장할 변수
answer = 0    # 총 비용

for i in range(n-1):
    if minCoast > coasts[i]:
        minCoast = coasts[i]

    answer += (minCoast * distances[i])

print(answer)