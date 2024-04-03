arr = list(map(int,input().split()))
su = 0
for i in range(len(arr)):
    if arr[i] % 3 == 0:
        su = arr[i-1]
        break
print(su)