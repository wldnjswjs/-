n = int(input())
lopeu = []
answers = []

for i in range(n):
    lopeu.append(int(input()))

lopeu.sort(reverse=True) # 내림차순으로 정렬 

for x in range(n):  # 내림차순 정리된 로프와 1부터 곱해서 최댓값을 구한다. 
    answers.append((x+1)*lopeu[x])

print(max(answers))