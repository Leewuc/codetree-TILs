n = int(input())
lines = []
inter_line = {}
cnt = 0
for _ in range(n):
    x1, x2 = map(int,input().split())
    lines.append((x1,x2))
for line in lines:
    for i in range(line[0],line[1]):
        if i in inter_line:
            inter_line[i] += 1
        else:
            inter_line[i] = 1
print(max(inter_line.values())+1)