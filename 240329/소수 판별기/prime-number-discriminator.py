n = int(input())
bb = False
for i in range(2,n):
    if n % i == 0:
        bb = True
if bb == True:
    print("C")
else:
    print("P")