# 입력 받기
a, b = map(int, input().split())
n = input()

# a진수를 10진수로 변환
decimal_n = int(n, a)

# 10진수를 b진수로 변환하여 출력
print(format(decimal_n, 'b'))