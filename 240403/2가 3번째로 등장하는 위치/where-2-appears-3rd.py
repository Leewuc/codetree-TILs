n = int(input())
numbers = list(map(int, input().split()))

count = 0
for idx, num in enumerate(numbers):
    if num == 2:
        count += 1
        if count == 3:
            print(idx + 1)
            break