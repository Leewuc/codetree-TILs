i = input()
arr = i.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
if a < b and b < c:
    print(a)
elif b < a and a < c:
    print(b)
else:
    print(c)