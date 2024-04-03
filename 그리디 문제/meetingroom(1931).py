n = int(input())

room = []

for i in range(n):
    st, et = map(int, input().split())
    room.append([st,et])

# 시작시간이 이르면서 끝나는 시간도 이른 순으로 정렬
room.sort(key= lambda x : x[0])
room.sort(key= lambda x : x[1])

cnt=1   # 회의 개수를 저장할 변수
end = room[0][1]    # 회의의 마지막 시간을 저장할 변수

for i in range(1,n):
    if room[i][0]>=end: # 시작시간이 회의의 마지막 시간보다 크거나 같을 경우
        cnt+=1
        end = room[i][1]

print(cnt)