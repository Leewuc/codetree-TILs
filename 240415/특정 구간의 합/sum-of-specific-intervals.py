# 전역 변수로 수열 A를 선언
A = []

# n, m 입력 받기
n, m = map(int, input().split())

# 수열 A 입력 받기
A = list(map(int, input().split()))

# 두 숫자쌍 a1부터 a2까지의 합을 구하는 함수
def calculate_sum(a1, a2):
    return sum(A[a1-1:a2])

# m개의 숫자쌍에 대해 합을 계산하여 출력
for _ in range(m):
    a1, a2 = map(int, input().split())
    print(calculate_sum(a1, a2))