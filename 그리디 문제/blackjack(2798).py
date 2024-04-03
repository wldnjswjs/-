n, m = map(int, input().split())
blackjack = list(map(int, input().split()))

count = 0
card = []

# 브루트 포스 방식으로 해결
for one in blackjack:
    for two in blackjack:
        for three in blackjack:
            max_sum = 0
            max_sum = one+two+three
            if max_sum <= m:
                if one != two and two != three and one != three:
                    card.append(max_sum)

print(max(card))