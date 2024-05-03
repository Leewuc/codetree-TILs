import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = [
	int(input())
	for _ in range(n)
]

min_dist = INT_MAX
# 각 i번째 집으로 모였을 때의 합을 구해줍니다.
for i in range(n):
	sum_dist = 0
	for j in range(n):
		dist = (j + n - i) % n
		sum_dist += dist * arr[j]
	
	# 가능한 거리의 합 중 최솟값을 구해줍니다.
	min_dist = min(min_dist, sum_dist)

print(min_dist)