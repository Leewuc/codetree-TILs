# 정수 n 입력 받기
n = int(input())

# 문자열 길이의 합과 'a'의 개수 초기화
total_length = 0
count_a = 0

# n개의 문자열 입력 받기
for _ in range(n):
    s = input()
    total_length += len(s)
    if s.startswith('a'):
        count_a += 1

# 결과 출력
print(total_length, count_a)