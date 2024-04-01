n = int(input())

# n x n 크기의 정사각형을 두 개 출력
for _ in range(2):
    for _ in range(n):
        print('*' * n)
    print()  # 공백 라인 출력