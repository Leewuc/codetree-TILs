i = input()
arr = i.split()
a = int(arr[0])
b = int(arr[1])
if a>b:
    print(a*b)
else:
    print(b//a)