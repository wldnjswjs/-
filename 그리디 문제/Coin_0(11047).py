n, k = map(int, input().split())    # n: 화폐 종류, k: 돈

coins = []                          # 동전 종류를 저장하는 리스트
answer = 0                          # 제출할 동전 개수

for _ in range(n):                  # 리스트에 동전 종류를 저장
    coins.append(int(input()))
coins.sort(reverse=True)            # 리스트를 역방향으로 바꾼다. 

for i in coins:                     
    answer += k//i                  # k에서 나눌 수 있는 가장 큰 화폐를 나누고
    k %= i                          # 나머지를 다음 단위 화폐로 나눈다. 

print(answer)