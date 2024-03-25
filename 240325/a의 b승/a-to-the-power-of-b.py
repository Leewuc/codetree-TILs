a1 = input()
arr = a1.split()
a = int(arr[0])
b = int(arr[1])
prod = 1
for i in range(1,b+1):
    prod *= a
print(prod)