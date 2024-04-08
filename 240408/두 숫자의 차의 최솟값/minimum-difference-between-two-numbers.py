n = int(input())
arr = list(map(int, input().split()))

# 숫자들이 오름차순으로 주어지기 때문에,
# 두 숫자의 차의 최솟값은 반드시 인접한 두 숫자의 차 중에 최솟값이 있습니다.
# 초기값을 적습니다. 최소가 될 첫 번째 후보입니다.
min_val = arr[1] - arr[0]

# 나머지 원소들을 보며 최솟값을 갱신합니다.
for i in range(2, n):
    if min_val > arr[i] - arr[i - 1]:# 지금까지 나왔던 값들 보다 더 작은 값이라면
	    min_val = arr[i] - arr[i - 1]  # 최솟값이 되므로 그 값을 갱신합니다.

print(min_val)