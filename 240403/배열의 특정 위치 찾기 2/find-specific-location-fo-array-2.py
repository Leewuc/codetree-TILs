arr = list(map(int,input().split()))
su1 = 0
su2 = 0
me1 = 0
me2 = 0
for i in range(0,10,2):
    su1 += arr[i]
for i in range(1,10,2):
    su2 += arr[i]
if su1 > su2:
    me1 = su1 - su2
    print(me1)
else:
    me2 = su2 - su1
    print(me2)