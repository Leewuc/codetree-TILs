n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def distance_squared(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

min_distance_squared = float('inf')

for i in range(n):
    for j in range(i+1, n):
        dist_sq = distance_squared(points[i][0], points[i][1], points[j][0], points[j][1])
        if dist_sq < min_distance_squared:
            min_distance_squared = dist_sq

print(min_distance_squared)