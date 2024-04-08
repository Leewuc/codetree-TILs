def print_grid(n, m, coins):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for r, c in coins:
        grid[r - 1][c - 1] = 1

    for row in grid:
        print(" ".join(map(str, row)))

# 입력 예제
n, m = map(int, input().split())
coins = []
for _ in range(m):
    coins.append(tuple(map(int, input().split())))

print_grid(n, m, coins)