def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 정수 N 입력 받기
N = int(input())

# N번째 피보나치 수 출력
print(fibonacci(N))