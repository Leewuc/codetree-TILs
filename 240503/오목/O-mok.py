grid = [list(map(int, input().split())) for _ in range(19)]
winner , mid_x, mid_y = 0,0,0

for i in range(19):
    for j in range(15):
        if grid[i][j] != 0:
            indicator = True
            for a in range(5):
                if grid[i][j] != grid[i][j+a]:
                    indicator = False
            tmp = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3] +grid[i][j+4]
            if ((tmp == 5) or (tmp == 10)) and indicator:
                winner = tmp//5
                mid_x, mid_y = i, j+2
for i in range(15):
    for j in range(19):
        if grid[i][j] != 0:
            indicator = True
            for a in range(5):
                if grid[i][j] != grid[i+a][j]:
                    indicator = False

            tmp = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j] + grid[i+4][j]
            if ((tmp == 5) or (tmp == 10)) and indicator:
                winner = tmp//5
                mid_x, mid_y = i+2, j
for i in range(15):
    for j in range(15):
        if grid[i][j] != 0:
            indicator = True
            for a in range(5):
                if grid[i][j] != grid[i+a][j+a]:
                    indicator = False

            tmp = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3] + grid[i+4][j+4]
            if ((tmp == 5) or (tmp == 10)) and indicator:
                winner = tmp//5
                mid_x, mid_y = i+2, j+2


for i in range(4, 19):
    for j in range(15):
        if grid[i][j] != 0:
            indicator = True
            for a in range(5):
                if grid[i][j] != grid[i-a][j+a]:
                    indicator = False
            tmp = grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] + grid[i-3][j+3] + grid[i-4][j+4]
            if (tmp == 5 or tmp ==10) and indicator:
                winner = tmp//5
                mid_x, mid_y = i-2, j+2

if winner == 0:
    print(0)
else:
    print(winner)
    print(mid_x+1, mid_y+1)
'''
def f(dx, dy):
    for i in range(19):
        for j in range(19):
            if not (
                grid[i][j]
                and 0 <= i + dx*4 < 19
                and 0 <= j + dy*4 < 19
            ):
                continue
            flag = True
            for k in range(5):
                flag &= grid[i][j] == grid[i + dx*k][j + dy*k]
            if flag:
                winner = grid[i][j]
                mid_x = i + dx*2
                mid_y = j + dy*2
'''