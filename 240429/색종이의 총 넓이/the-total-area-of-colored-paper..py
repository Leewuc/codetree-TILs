n = int(input())

OFFSET = 100
blocks = [[0 for _ in range(100 + OFFSET + 1)] for _ in range(100 + OFFSET + 1)]

area = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    a += OFFSET
    b += OFFSET 

    for j in range(a, a + 8):
        for k in range(b, b + 8):
            blocks[j][k] = 1

for i in range(100 + OFFSET + 1):
    for j in range(100 + OFFSET + 1):          
        if blocks[i][j] == 1:
            area += 1
print(area)