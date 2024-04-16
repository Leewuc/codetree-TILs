n = input()
n1 = input()
n2 = list(n)
n3 = list(n)
n2.sort()
n3.sort()
boo = False
for i in range(len(n)):
    if len(n) != len(n1):
        boo = False
    elif n2[i] == n3[i]:
        boo = True       
    else:
        boo = False
if boo == True:
    print("Yes")
else:
    print("No")