import sys; 
input = sys.stdin.readline

n = int(input())
candy = list(map(int, input().split()))

oddcandy = []
result = 0

for i in candy:
    if i%2 == 0:
        result += i
    else:
        oddcandy.append(i)

if len(oddcandy)%2 != 0:
    oddcandy.sort(reverse=True)
    del oddcandy[-1]
    result += sum(oddcandy)
else:
    result += sum(oddcandy)

print(result)