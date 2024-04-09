# 문자열을 입력 받습니다.
s = input()

# 소문자로 변환하여 출력합니다.
result = ''.join(c.lower() for c in s if c.isalnum())
print(result)