N = int(input())
numbers = list(map(int, input().split()))

count = 0
for start in range(N):
    for end in range(start, N):
        subarray = numbers[start:end+1]
        average = sum(subarray) / len(subarray)
        if average in subarray:
            count += 1

print(count)