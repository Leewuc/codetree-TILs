arr = list(map(int, input().split()))

# for문을 한 번만 돌리는 경우
maxi = 1
mini = 1000
for i in range(10):
    if arr[i] < 500 and maxi <= arr[i]: # under
        maxi = arr[i]
    elif arr[i] > 500 and mini >= arr[i]: # over
        mini = arr[i]
print(maxi, mini)