i1 = input()
i2 = input()
arr1 = i1.split()
arr2 = i2.split()
a,b = int(arr1[0]),int(arr1[1])
c,d = int(arr2[0]),int(arr2[1])
if a > c:
    print("A")
elif c > a:
    print("B")
elif a == c and b > d:
    print("A")
else:
    print("B")