n = int(input())

# 삼각형 위쪽 부분 출력
for i in range(n, 0, -1):
    print('  ' * (n - i) + '* ' * (2*i-1))

# 삼각형 아래쪽 부분 출력
for i in range(2, n+1):
    print('  ' * (n - i) + '* ' * (2*i-1))