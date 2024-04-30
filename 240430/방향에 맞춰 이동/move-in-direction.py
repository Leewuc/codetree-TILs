n = int(input())
dx,dy = [1,0,-1,0],[0,-1,0,1]
x_1,y_1 = 0,0
for i in range(n):
    x,y = tuple(map(str,input().split()))
    y = int(y)
    if x == 'E':
        mo = 0
    elif x == 'S':
        mo = 1
    elif x == 'W':
        mo = 2
    else:
        mo = 3
    x_1 += dx[mo] * y
    y_1 += dy[mo] * y
print(x_1,y_1)