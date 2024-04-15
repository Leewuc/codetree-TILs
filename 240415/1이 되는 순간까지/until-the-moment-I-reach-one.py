# n 이 짝수이면 2 로 나누고
# n 이 홀수이면 3 으로 나눈 몫
# 값이 1이되면 모든 횟수를 구하는 작업


n = int(input())

def recursive(m):
    if m == 1:
        return 0
    if m % 2 == 0:
        return recursive(m // 2) + 1
    else:
        return recursive(m // 3) + 1

print(recursive(n))