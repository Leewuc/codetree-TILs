n = int(input())

# n * n 모양 정사각형 출력
for i in range(n):
    for j in range(n):
        print((2*i + 11) + 2*j, end=" ")
    print()