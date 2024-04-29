n = int(input())
offset = 100
MAX_R = 201
checked = [[0] * MAX_R for _ in range(MAX_R)]
area = 0

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x2 + offset, y2 + offset

    color = 2 if i % 2 == 1 else 1

    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = color

for x in range(MAX_R):
    for y in range(MAX_R):
        if checked[x][y] == 2:
            area += 1

print(area)