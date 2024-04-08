# 입력 받기
n = int(input())
strings = [input() for _ in range(n)]
start_char = input()

# 주어진 문자로 시작하는 문자열들 찾기
start_strings = [string for string in strings if string.startswith(start_char)]
num_start_strings = len(start_strings)
avg_length = round(sum(len(string) for string in start_strings) / num_start_strings, 2)

# 결과 출력
print(num_start_strings, f'{avg_length:.2f}')