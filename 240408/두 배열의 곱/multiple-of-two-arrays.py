n = 3
lst = [
    [0 for _ in range(n)]
    for _ in range(n)
]
lst1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]
cnt = 1
ccnt = 2
lst2 = [0][0] * n
for i in range(n):
    for j in range(n):
        lst[i][j] = cnt
        lst1[i][j] = ccnt
        cnt += 1
        ccnt += 1
        lst2 = lst[i][j] * lst1[i][j]
        print(lst2,end=" ")
    print()