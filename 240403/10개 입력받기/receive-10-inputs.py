arr = list(map(int,input().split()))
dec = []
su = 0
mea = 0
for i in range(len(arr)):
    if arr[i] == 0:
        break
    dec.append(arr[i])
    su = sum(dec)
    mea = su / len(dec)
print(su,f"{mea:.1f}")