n = int(input())

numbers = list(map(int,input().split()))
count = 1

for i in range(n-1):
    if (numbers[i] + numbers[i+1]) % 2 == 1:
        count += 1

print(*count)