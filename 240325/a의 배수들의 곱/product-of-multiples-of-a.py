a1 = input()
arr = a1.split()
a = int(arr[0])
b = int(arr[1])
prod = 1
for i in range(a,b+1,a):
        prod *= i
print(prod)