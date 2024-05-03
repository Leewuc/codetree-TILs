import sys
n = int(input())
n1 = list(map(int,input().split()))
max_t = 0
max_t2 = []
for i in range(n):
    for j in range(i+2,n):
        max_t = n1[i] + n1[j]
        max_t2.append(max_t)
print(max(max_t2))