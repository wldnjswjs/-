n, m = map(int, input().split())

card = []
count = 0

for i in range(m):
    a, b = map(int, input().split())
    card.append([a, b])

card.sort(key= lambda x: x[0])

for i in range(1, m):
    if card[i][0] < n:
        count += n - card[i][0]

print(count)