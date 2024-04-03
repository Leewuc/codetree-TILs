nums = list(map(int, input().split()))
new = []
for i in range(len(nums)):
    if nums[i] == 0:
        break
    new.append(nums[i])

for i in new[::-1]:
    print(i, end=' ')