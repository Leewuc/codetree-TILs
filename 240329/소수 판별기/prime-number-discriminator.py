n = int(input())
bb = False
for i in range(1,n+1):
    if n % i != 0:
        bb = True
if bb == True:
    print("P")
else:
    print("C")