import sys
INT_MAX = sys.maxsize
n = list(map(int,input().split()))

def get_diff(i,j,k):
    sum1 = n[i] + n[j] + n[k]
    sum2 = sum(n) - sum1
    return abs(sum1-sum2)

min_diff = INT_MAX
for i in range(0,6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            min_diff = min(min_diff,get_diff(i,j,k))
print(min_diff)