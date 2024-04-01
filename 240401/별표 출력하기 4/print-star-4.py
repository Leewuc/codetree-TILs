n = int(input())

# 위쪽 삼각형 출력
for i in range(n, 0, -1):
    print('* ' * i)

# 아래쪽 삼각형 출력
for i in range(2, n+1):
    print('* ' * i)