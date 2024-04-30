n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_length = 0
length = 0

for num in arr:
    if num > t:
        length += 1
        max_length = max(max_length, length)
    else:
        length = 0

print(max_length)