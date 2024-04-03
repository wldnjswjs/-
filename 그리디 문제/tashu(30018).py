n = int(input())
before = list(map(int, input().split()))
after = list(map(int, input().split()))
sum = 0

for i in range(n):
    if before[i] > after[i]:
        sum += before[i] - after[i]

print(sum)