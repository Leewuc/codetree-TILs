from itertools import combinations

def min_diff(arr):
    two_combinations = list(combinations(arr, 2))
    
    min_diff = float('inf')
    for two in two_combinations:
        remaining = arr.copy()
        remaining.remove(two[0])
        remaining.remove(two[1])
        
        for other_two in combinations(remaining, 2):
            last_one = remaining.copy()
            last_one.remove(other_two[0])
            last_one.remove(other_two[1])
            
            team_sums = [sum(two), sum(other_two), last_one[0]]
            
            if len(set(team_sums)) != len(team_sums):
                continue
            
            diff = max(team_sums) - min(team_sums)
            if diff < min_diff:
                min_diff = diff
                
    return -1 if min_diff == float('inf') else min_diff


arr = list(map(int, input().split()))
print(min_diff(arr))