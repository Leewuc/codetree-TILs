r,c = map(int,input().split())
lst = [list(map(str,input().split())) for _ in range(r)]
cnt = 0
for i in range(1,r):
    for j in range(1,c):
        for k in range(i+1,r-1):
            for l in range(j+1,c-1):
                if lst[0][0] != lst[i][j] and lst[i][j] != lst[k][l] and lst[k][l] != lst[r-1][c-1]:
                    cnt+=1
print(cnt)