n = int(input())

arr = list(map(int,input().split()))

min_val = arr[0]
for i in range(n):
    if min_val > arr[i]:
        min_val = arr[i]

count = 0
for elem in arr:
    if elem == min_val:
       count += 1

print(min_val, count)