a,b,c = map(int,input().split())
bb = False
for i in range(a,b+1):
    if (c % i) == 0:
        bb == True
if bb == True:
    print("NO")
else:
    print("YES")