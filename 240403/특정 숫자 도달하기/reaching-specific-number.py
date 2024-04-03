arr = list(map(int, input().split()))

# 마지막으로 주어진 수를 제외하고 '현재까지' 주어진
i = 0
sum_val = 0
for i in range(len(arr)):
    sum_val += arr[i]
    if arr[i] >= 250:
        sum_val -= arr[i]
        i -= 1
        break

avg_val = sum_val / (i + 1)
print(sum_val, "{:.1f}".format(avg_val))