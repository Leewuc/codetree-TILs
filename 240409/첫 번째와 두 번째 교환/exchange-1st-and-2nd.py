# 문자열을 입력 받습니다.
input_str = input()

# 첫 번째 문자와 두 번째 문자를 저장합니다.
first_char, second_char = input_str[0], input_str[1]

# 문자열을 반복하면서 조건에 맞게 문자를 교체합니다.
result = ""
for char in input_str:
    if char == first_char:
        result += second_char
    elif char == second_char:
        result += first_char
    else:
        result += char

# 결과를 출력합니다.
print(result)