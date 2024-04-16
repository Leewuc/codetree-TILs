n, k, T = list(input().split())
n, k = int(n), int(k)
nums = []
T_nums = []

for _ in range(n):
    nums.append(input())

for i in nums:
    if len(i) > len(T):
        if i[0:len(T)] == T:
            T_nums.append(i)

T_nums.sort()
print(T_nums[k-1])