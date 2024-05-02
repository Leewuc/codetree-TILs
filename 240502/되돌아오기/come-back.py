n = int(input())
dirc = [list(map(str, input().split())) for _ in range(n)]

count = 0
total = 0

for i in range(n):
    dirc[i][1] = int(dirc[i][1])
    total += dirc[i][1]

def move(string, x, y):
    if string == 'N':
        return x-1, y
    elif string == 'E':
        return x, y+1
    elif string == 'S':
        return x+1, y
    elif string == 'W':
        return x, y-1

n1, n2 = n, n

a = 0
for j in range(n):
    for k in range(dirc[j][1]):
        n1, n2 = move(dirc[j][0], n1, n2)
        count += 1
        a += 1
        if n == n1 and n == n2:
            print(count)
            break   
        elif a == total:
            print(-1)
            break
    if n == n1 and n == n2:
        break