n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    total = sum([num for num in range(a, b+1) if num % 2 == 0])
    print(total)