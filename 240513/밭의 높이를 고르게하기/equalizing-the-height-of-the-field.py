def calculate_cost(heights, start, end, target_height):
    cost = 0
    for i in range(start, end):
        if heights[i] < target_height:
            cost += target_height - heights[i]
        elif heights[i] > target_height:
            cost += heights[i] - target_height
    return cost

def find_min_cost(N, H, T, heights):
    min_cost = float('inf')
    for start in range(N - T + 1):
        end = start + T
        cost = calculate_cost(heights, start, end, H)
        min_cost = min(min_cost, cost)
    return min_cost

# 입력 받기
N, H, T = map(int, input().split())
heights = list(map(int, input().split()))

# 최소 비용 계산
min_cost = find_min_cost(N, H, T, heights)

# 출력
print(min_cost)