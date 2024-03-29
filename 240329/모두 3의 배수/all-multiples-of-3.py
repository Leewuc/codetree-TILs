bb = False
for i in range(1,6):
    n = int(input())
    if n % 3 == 0:
        bb = True
if bb == True:
    print(1)
else:
    print(0)