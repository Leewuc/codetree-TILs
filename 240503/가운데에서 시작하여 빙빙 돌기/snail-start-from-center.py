n = int(input())

answer = [
    [0]*n
    for _ in range(n)
]

x = n-1
y = n-1

dir_num = 0
dxs,dys = [0, -1, 0, 1], [-1, 0, 1, 0]
answer[x][y] = n*n

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(n*n-1,0,-1):
    nx,ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx,ny) or answer[nx][ny]!=0:
        dir_num = (dir_num+1)%4
    x,y = x+dxs[dir_num], y+dys[dir_num]
    answer[x][y] = i

for i in range(n):
    for j in range(n):
        print(answer[i][j], end =" ")
    print()