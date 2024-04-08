# 10개의 문자열 입력 받기
strings = [input() for _ in range(10)]

# 끝 문자 입력 받기
end_char = input()

# 주어진 문자로 끝나는 문자열 찾아서 출력하기
found = False
for string in strings:
    if string.endswith(end_char):
        print(string)
        found = True

# 만약 주어진 문자로 끝나는 문자열이 없으면 'None' 출력
if not found:
    print('None')