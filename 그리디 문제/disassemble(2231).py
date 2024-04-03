n = int(input())
result = 0

# 브루트 포스 방식으로 해결
for i in range(1,n+1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == n:
        print(i)
        break
    if i == n:
        print(0)