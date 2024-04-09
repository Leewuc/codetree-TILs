def min_shift(a, b):
    if a == b:
        return 0
    
    n = len(a)
    for i in range(1, n):
        if a[-i:] + a[:-i] == b:
            return i
    return -1

# 입력 받기
a = input().strip()
b = input().strip()

# 결과 출력
print(min_shift(a, b))