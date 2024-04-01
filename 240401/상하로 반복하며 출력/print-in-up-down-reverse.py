n = int(input())

# n값에 따라 일의 자리 숫자를 상하로 반복하여 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        print((i + j - 1) % n + 1, end="")
    print()