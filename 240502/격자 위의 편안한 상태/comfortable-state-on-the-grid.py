n,m = tuple(map(int,input().split()))
qq = [[0]*(n+2) for _ in range(n+2)]
dx,dy = [0,1,0,-1],[1,0,-1,0]
for _ in range(m):
    x,y = tuple(map(int,input().split()))
    qq[x][y] = 1
    cnt = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if qq[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)