n = int(input())

color = [0] * 2001
cur = 1000

for _ in range(n):
    a, b = input().split()
    a = int(a)

    if b == 'L':
        left = cur - a
        for i in range(max(left, 0), min(cur, 2001)):
            color[i] = 1  # 흰색 타일로 설정
        cur = left

    elif b == 'R':
        right = cur + a
        for i in range(max(cur, 0), min(right, 2001)):
            color[i] = 2  # 검은색 타일로 설정
        cur = right

wh = color.count(1)
bl = color.count(2)

print(wh, bl)