def max_workload(N, C, G, H, temperature_ranges):
    # 가능한 모든 온도를 탐색하기 위해 온도를 0에서 1000까지 순회합니다.
    max_workload = 0
    
    for temperature in range(1001):
        current_workload = 0
        
        for Ta, Tb in temperature_ranges:
            if temperature < Ta:
                current_workload += C
            elif Ta <= temperature <= Tb:
                current_workload += G
            else:
                current_workload += H
        
        # 최대 작업량을 업데이트합니다.
        if current_workload > max_workload:
            max_workload = current_workload
    
    return max_workload

# 입력을 받습니다.
N, C, G, H = map(int, input().split())
temperature_ranges = [tuple(map(int, input().split())) for _ in range(N)]

# 최대 작업량을 계산합니다.
result = max_workload(N, C, G, H, temperature_ranges)
print(result)