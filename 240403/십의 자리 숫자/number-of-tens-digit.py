counts = [0] * 10
nums = list(map(int, input().split()))

for num in nums:
    if num == 0:
        break
    tens_digit = num // 10
    counts[tens_digit] += 1

for i in range(1, 10):
    print(f"{i} - {counts[i]}")