i1 = input()
i2 = input()
arr1 = i1.split()
arr2 = i2.split()
a = int(arr1[0])
b = int(arr1[1])
c = int(arr2[0])
d = int(arr2[1])
if a > c and b > d:
    print(1)
else:
    print(0)