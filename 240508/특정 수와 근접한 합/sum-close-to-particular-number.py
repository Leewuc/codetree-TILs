import sys
n,s = tuple(map(int,input().split()))
lst = list(map(int,input().split()))
s_val = sys.maxsize
sums = sum(lst)
for i in range(n):
    sum_val = 0
    for j in range(i+1,n):
        sum_val = lst[i] + lst[j]
        s_val = min(s_val,abs(s-(sums-sum_val)))
print(s_val)