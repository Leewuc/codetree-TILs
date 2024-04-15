def print_increasing(n):
    if n == 0:
        return
    print_increasing(n - 1)
    print(n, end=" ")

def print_decreasing(n):
    if n == 0:
        return
    print(n, end=" ")
    print_decreasing(n - 1)

# 정수 N 입력 받기
N = int(input())

# 1부터 N까지 출력하는 함수 호출
print_increasing(N)
print()

# N부터 1까지 출력하는 함수 호출
print_decreasing(N)