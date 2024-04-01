n = int(input())

# 패턴 출력
for i in range(n*2+1):
    if i % 2 == 0:
        print('* ' * (2*n+1))
    else:
        print('*   ' * (n) + '*')