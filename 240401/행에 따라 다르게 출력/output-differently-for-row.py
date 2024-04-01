n = int(input())

start = 1
for i in range(n):
    line = []
    for j in range(n):
        line.append(start)
        start += 2 if i % 2 == 1 else 1
    start += -1 if i % 2 == 1 else 1
    print(*line)