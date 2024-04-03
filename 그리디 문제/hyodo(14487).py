n = int(input())
moneys = list(map(int, input().split()))

moneys.sort()
sum = 0

for i in range(n-1):
    sum += moneys[i]

print(sum)