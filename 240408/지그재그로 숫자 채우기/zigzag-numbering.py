def zigzag(n, m):
    arr = [[0 for _ in range(m)] for _ in range(n)]

    num = 0
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                arr[i][j] = num
                num += 1
        else:
            for j in range(m - 1, -1, -1):
                arr[i][j] = num
                num += 1

    return arr

n, m = 4, 2  # 지그재그 모양을 만들 크기 입력
result = zigzag(n, m)
for row in result:
    print(' '.join(map(str, row)))