import heapq
import sys

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    num = int(input())
    heapq.heappush(cards, num)

result = 0  # 카드 묶음을 합친 결과 
while len(cards)>1:
    n1 = heapq.heappop(cards)
    n2 = heapq.heappop(cards)
    result += n1 + n2   # 가장 작은 카드 두묶음을 꺼내서 합친다. 
    heapq.heappush(cards, n1+n2)    # 합친 결과를 다시 큐에 넣는다. 

print(result)

'''
n = int(input())

cards = []

for i in range(n):
    cards.append(int(input()))

cards.sort

answer = cards[0] + cards[1]

for i in range(2, n):
    answer = answer + cards[i] + answer

print(answer)
'''