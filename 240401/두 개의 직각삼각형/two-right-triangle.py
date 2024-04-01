n = int(input())

# 삼각형 위쪽 부분 출력
for i in range(n, 0, -1):
    print('*' * i + '  ' * (n - i) + '*' * i)