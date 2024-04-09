# 문자열과 찾을 문자를 입력 받습니다.
string, char = input().split()

# 문자의 위치를 찾습니다.
index = string.find(char)

# 문자의 위치를 출력합니다.
if index != -1:
    print(index)
else:
    print("No")