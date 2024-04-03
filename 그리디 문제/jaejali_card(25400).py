n = int(input())
a = list(map(int, input().split()))
count = 0
j = 1

for i in range(n):
    if a[i] != j:
        count += 1
    else:
        j += 1

print(count)