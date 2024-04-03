n = int(input())
arr = []

arr.append(1)
arr.append(n)

for i in range(2,10):
    arr.append(arr[i-1]+arr[i-2])

for elem in arr:
    
    print(elem,end=" ")
    if elem > 100:
        break