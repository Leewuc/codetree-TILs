i1 = input()
i2 = input()
arr1 = i1.split()
arr2 = i2.split()
a,b = int(arr1[0]),str(arr1[1])
c,d = int(arr2[0]),str(arr2[1])
if (b =='M' and a >=19) or (d == 'M' and c >=19):
    print(1)
else:
    print(0)