i = input()
arr = i.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
if a < b and b < c and a < c:
    print(a)
elif b < a and a < c and b < c:
    print(b)
elif c < a and c < b and b < a:
    print(c)