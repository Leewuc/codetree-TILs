a,b,c = map(int,input().split())
bb = True
for i in range(a,b+1):
    if (i % c) == 0:
        bb = False
if bb == True:
    print("YES")
else:
    print("NO")