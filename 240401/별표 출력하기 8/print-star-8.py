n = int(input())

# 별표 출력
for i in range(1, n+1):
    if i % 2 != 0:
        print('*')
    else:
        print('* ' * i)