s = input().split('-') # '-'를 기준으로 split해서 리스트에 저장
answer = 0             # 최솟값을 저장할 변수

for i in s[0].split('+'):   # 덧셈을 위해 '+'를 기준으로 split
    answer += int(i)        # split한 값을 다 더한다. 

for i in s[1:]:             # '-'를 만난 이후이므로
    for j in i.split('+'):  # '+'를 기준으로 split하고
        answer -= int(j)    # 이 값들을 answer에서 모두 빼주면 된다. 

print(answer)