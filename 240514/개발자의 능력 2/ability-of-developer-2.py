from itertools import combinations

def find_min_diff(arr):
    # 6명 중 2명, 4명을 뽑는 모든 조합을 생성
    two_combinations = list(combinations(arr, 2))
    
    min_diff = float('inf')
    
    # 모든 두 명 조합에 대하여
    for two in two_combinations:
        remaining = arr.copy()
        
        # 두 명을 제외한 나머지에서 다시 두 명을 뽑는 조합
        remaining.remove(two[0])
        remaining.remove(two[1])
        
        for other_two in combinations(remaining, 2):
            last_two = remaining.copy()
            last_two.remove(other_two[0])
            last_two.remove(other_two[1])
            
            # 각 팀의 능력치 합산
            team_sums = [sum(two), sum(other_two), sum(last_two)]
            
            # 최대 팀과 최소 팀간의 차이 계산
            diff = max(team_sums) - min(team_sums)
            
            # 최소 차이 갱신
            if diff < min_diff:
                min_diff = diff
                
    return min_diff

# 입력 예제
arr = list(map(int, input().split()))
print(find_min_diff(arr))