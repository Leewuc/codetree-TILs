n = int(input())
dir_s = {
    0:1,
    1:0,
    2:3,
    3:2
}
dir_r = {
    0:3,
    1:2,
    2:1,
    3:0
}
dir_a = {
    0:2,
    1:3,
    2:0,
    3:1,
}
dx,dy = [1,0,-1,0],[0,-1,0,1]
grid = []
cnt = 0
for i in range(n):
    grid.append(list(input()))
k = int(input())
dir_f = 0
r,c = 0,0
if k <= n:
    dir_f = 0
    r,c = 0,k-1
elif k > n and k <= 2*n:
    dir_f = 1
    r,c = k-n-1, n-1
elif k > 2*n and k <= 3*n:
    dir_f = 2
    r,c = n-1,3*n-k
elif k > 3*n:
    dir_f = 3
    r,c = 4*n-k,0

while r >= 0 and r < n and c>=0 and c < n:
    if grid[r][c] == '/':
        dir_f = dir_s[dir_f]
    elif grid[r][c] == '\\':
        dir_f = dir_r[dir_f]
    r,c = r+dx[dir_f],c+dy[dir_f]
    cnt += 1
print(cnt)