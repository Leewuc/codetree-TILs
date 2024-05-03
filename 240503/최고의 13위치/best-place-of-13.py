n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
max_cnt = 0
for i in range(n):
    for j in range(n-2):
        max_cnt = max(max_cnt,lst[i][j] + lst[i][j+1] + lst[i][j+2])
print(max_cnt)