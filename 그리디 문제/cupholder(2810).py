n = int(input()) # 좌석 수
member = input() # 좌석 정보

count = member.count('LL') # 커플석의 개수

if (count <= 1):
    print(n)

else:
    print(n + 1 - count)