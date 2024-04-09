# 입력 문자열 A와 B를 받습니다.
a = input()
b = input()

# A에서 B를 지우는 과정을 반복합니다.
while b in a:
    a = a.replace(b, '', 1)

# 결과를 출력합니다.
print(a)