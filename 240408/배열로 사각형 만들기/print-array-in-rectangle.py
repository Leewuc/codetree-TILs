# 5x5 배열 초기화
arr = [[0 for _ in range(5)] for _ in range(5)]

# 첫 번째 행과 첫 번째 열을 1로 초기화
for i in range(5):
    arr[i][0] = 1
for j in range(5):
    arr[0][j] = 1

# 나머지 칸들은 위의 값과 왼쪽의 값을 더함
for i in range(1, 5):
    for j in range(1, 5):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

# 배열 출력
for i in range(5):
    for j in range(5):
        print(arr[i][j], end=' ')
    print()