# 입력 받기
string = input()

# 짝수 번째 문자만 역순으로 출력
print(string[1::2][::-1], end='')