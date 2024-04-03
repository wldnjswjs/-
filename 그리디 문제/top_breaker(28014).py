n = int(input())
tops = list(map(int,input().split()))
count = 1

for i in range (len(tops)-1):
    if tops[i] <= tops[i+1]:
        count += 1

print(count)