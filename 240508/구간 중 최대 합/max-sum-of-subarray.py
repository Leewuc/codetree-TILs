n, k = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum = sum(numbers[:k])  # 처음 k개의 숫자를 더한 값으로 초기화
current_sum = max_sum

for i in range(1, n - k + 1):
    current_sum = current_sum - numbers[i - 1] + numbers[i + k - 1]  # 이전 윈도우의 첫 번째 숫자를 빼고 새로운 숫자를 더함
    max_sum = max(max_sum, current_sum)  # 최댓값 갱신

print(max_sum)