n = int(input())
cnt = 0
lst = [int(input()) for _ in range(n)]
for i in range(n):
    if i==0 or lst[i] != lst[i-1]:
        cnt += 1
    elif lst[0] == lst[n-1]:
        cnt = n
print(cnt)