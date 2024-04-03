arr = list(map(int,input().split()))
dec = []
cnt = 0
su = 0
for i in range(len(arr)):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        dec.append(arr[i])
        su = sum(dec)        
        cnt += 1
print(cnt,su)