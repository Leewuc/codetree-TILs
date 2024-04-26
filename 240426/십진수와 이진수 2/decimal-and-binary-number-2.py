# 입력 받기
N = input()

# 2진수를 10진수로 변환하여 17배 한 후 다시 2진수로 변환하여 출력
result = bin(int(N, 2) * 17)[2:]
print(result)