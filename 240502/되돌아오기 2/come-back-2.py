string = input()
x,y = 0,0

# 시계 방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]

t = 0
direction = 3
flag = False
for i in string:
    t += 1
    if i == 'F':
        x += dx[direction]
        y += dy[direction]
    elif i == 'L':
        direction = (direction-1) % 4
    elif i == 'R':
        direction = (direction+1) % 4
    if x == 0 and y == 0:
        flag = True
        break
        
if flag is True:
    print(t)
else:
    print(-1)