def check_different_letters(s):
    unique_letters = set(s)
    return "Yes" if len(unique_letters) >= 2 else "No"

# 입력 받기
s = input()

# 결과 출력
print(check_different_letters(s))