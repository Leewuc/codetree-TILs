a,b,c = map(int, input().split())
satisefite = False


for i in range(a, b + 1):
    if i % c == 0:
        satisefite = True

if satisefite == True:
    print("YES")
else:
    print("NO")