n = int(input()) # 설탕 무게
count = 0 # 봉지 개수

while n>0:
    if n%5 == 0:   # 5의 배수일 경우
        count += n//5
        print(count)
        break
    n -= 3  # 5의 배수가 될 때까지 3씩 빼기
    count += 1 # 봉지 개수 1증가
else:
    print(-1) # 정확하게 n킬로그램을 만들 수 없다면