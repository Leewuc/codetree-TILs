i1 = input()
i2 = input()
i3 = input()
arr1 = i1.split()
arr2 = i2.split()
arr3 = i3.split()
a,b = str(arr1[0]),int(arr1[1])
c,d = str(arr2[0]),int(arr2[1])
e,f = str(arr3[0]),int(arr3[1])
if a == 'Y' and c == 'Y' and e == 'Y':
    if b >= 37 and d >= 37:
        print("E")
    elif d>=37 and f>=37:
        print("E")
    elif b >= 37 and f>= 37:
        print("E")
    else:
        print("N")
if a=='Y' and c == 'Y':
    if b >= 37 and d >= 37:
        print("E")
    elif d>=37 and f>=37:
        print("E")
    elif b >= 37 and f>= 37:
        print("E")
    else:
        print("N")
if c == 'Y' and e == 'Y':
    if b >= 37 and d >= 37:
        print("E")
    elif d>=37 and f>=37:
        print("E")
    elif b >= 37 and f>= 37:
        print("E")
    else:
        print("N")
if a == 'Y' and e == 'Y':
    if b >= 37 and d >= 37:
        print("E")
    elif d>=37 and f>=37:
        print("E")
    elif b >= 37 and f>= 37:
        print("E")
    else:
        print("N")
else:
    print("N")