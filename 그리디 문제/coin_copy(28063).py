n = int(input())
x, y = map(int, input().split())
square = [[0 for _ in range(n)] for _ in range(n)]
square[n-y][x-1] = 1

if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    if square[0][0] == 1 or square[0][n-1] == 1 or square[n-1][0] == 1 or square[n-1][n-1] == 1:
        print(2)
    
    for i in range(1,n-1):
        if square[0][i] == 1 or square[i][0] == 1:
            print(3)
        
    for i in range(1,n-1):
        if square[i][n-1] == 1 or square[n-1][i] == 1:
            print(3)
            
    for i in range(1,n-1):
        for j in range(1,n-1):
            if square[i][j] == 1:
                print(4)
