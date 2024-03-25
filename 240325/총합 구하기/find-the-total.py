a1 = input()
arr = a1.split()
a = int(arr[0])
b = int(arr[1])
n = 0
for i in range(a,b+1):
    if(i % 6 == 0 and i % 8 !=0):
        n += i
print(n)