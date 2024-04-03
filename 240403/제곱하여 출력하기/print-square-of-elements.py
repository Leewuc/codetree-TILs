n = int(input())
arr = list(map(int, input().split()))
sq_arr =[]
for x in arr:
    sq_arr.append(x*x)

print(*sq_arr)