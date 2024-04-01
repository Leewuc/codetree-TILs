n = int(input())

# 역삼각형 위쪽 부분 출력
for i in range(n):
    print('  ' * i + '* ' * (2*n-1-2*i))