n = int(input())
milks = list(map(int, input().split()))
count = 0

for i in range(n):
    if (milks[i] == count % 3):
        count += 1

print(count)