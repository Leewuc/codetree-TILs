arr = list(map(int, input().split()))
su = 0
for i in range(1,10,2):
    su += arr[i]
me = 0
me = arr[2] + arr[5] + arr[8]
mea = 0
mea = me / 3
print(su,f"{mea:.1f}")