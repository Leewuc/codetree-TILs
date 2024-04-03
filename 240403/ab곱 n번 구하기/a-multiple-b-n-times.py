n = int(input())

for _ in range(n):
	a,b = map(int,input().split())
	ans = 1
	# a부터 b까지 전부 곱한 값을 출력합니다.
	for i in range(a, b + 1):
		ans *= i
	print(ans)