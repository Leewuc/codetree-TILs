def convert_base(n, base):
    if n < base:
        return str(n)
    else:
        return convert_base(n // base, base) + str(n % base)

# 입력 받기
N, B = map(int, input().split())

# 결과 출력
print(convert_base(N, B))