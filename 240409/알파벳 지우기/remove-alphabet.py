# 두 개의 문자열을 입력 받습니다.
s1 = input()
s2 = input()

# 문자열에서 숫자만 추출하여 정수로 변환합니다.
def extract_numbers(s):
    return int(''.join(filter(str.isdigit, s)))

# 두 수를 추출하고 더한 값을 출력합니다.
result = extract_numbers(s1) + extract_numbers(s2)
print(result)