# 5개의 문자열 초기화
strings = ["apple", "banana", "grape", "blueberry", "orange"]

# 영문자 하나 입력 받기
char = input()

# 세 번째나 네 번째 문자와 일치하는 문자열 찾기
count = 0
for string in strings:
    if len(string) >= 4 and (string[2] == char or string[3] == char):
        print(string)
        count += 1

# 조건을 만족하는 문자열의 개수 출력
print(count)