n,m = tuple(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
cnt = 0
for i in range(n-m+1):
    chk = True
    find = arr2[:]
    for j in range(m):
        if arr1[i+j] in find:
            find.pop(find.index(arr1[i+j]))
        else:
            chk = False
            break
    if chk is True:
        cnt += 1
print(cnt)