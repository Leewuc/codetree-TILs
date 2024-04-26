def solution(k,j):
    arr = []
    while(k>0):
        arr.append(str(k%j))
        k = k//j
    arr.reverse()
    return ''.join(arr)
    
a,b = map(int,input().split())
n = input()
s = int(n,a)

print(solution(s,b))