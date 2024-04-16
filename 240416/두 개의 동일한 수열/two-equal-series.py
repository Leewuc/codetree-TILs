n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1.sort()
arr2.sort()
boo = False
for i in range(n):
    if arr1[i] == arr2[i]:
        boo = True
    else:
        boo = False
if boo == True:
    print("Yes")
else:
    print("No")