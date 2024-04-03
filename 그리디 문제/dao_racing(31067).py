n, k = map(int, input().split())
track = list(map(int, input().split()))
count = 0

for i in range(n-1):
    if track[i] < track[i+1]:
        continue
    else:
        track[i+1] += k
        count += 1

sign = 0
for i in range(n-1):
    if track[i] < track[i+1]:
        continue
    else:
        sign = 1
        break

if sign == 0:
    print(count)
else:
    print(-1)