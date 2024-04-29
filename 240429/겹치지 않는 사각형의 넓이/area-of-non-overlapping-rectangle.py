map_data = [list(map(int,input().split())) for _ in range(2)]
delete_data = [list(map(int,input().split())) for _ in range(1)]


offset = 1000
check_area = [[0] * 2001 for _ in range(2001)]

# delete area 는 -1로 채웁니다.
for x1, y1, x2, y2 in delete_data:
    x1, y1 = x1+offset, y1+offset
    x2, y2 = x2+offset, y2+offset

    for x in range(x1,x2):
        for y in range(y1,y2):
            check_area[x][y] -= 1

# map data area 는 1을 더합니다.
for x1, y1,x2, y2 in map_data:
    x1, y1 = x1+offset, y1+offset
    x2, y2 = x2+offset, y2+offset


    for x in range(x1,x2):
        for y in range(y1,y2):
            check_area[x][y] += 1

# map data area에서 1인 거의 갯수.
cnt = 0
for x in range(2001):
    for y in range(2001):
        if check_area[x][y] == 1:
            cnt += 1

print(cnt)