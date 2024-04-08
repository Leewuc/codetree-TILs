# 세 줄에 걸쳐 문자열 입력 받기
string1 = input()
string2 = input()
string3 = input()

# 문자열 길이 차이 계산
min_length = min(len(string1), len(string2), len(string3))
max_length = max(len(string1), len(string2), len(string3))
difference = max_length - min_length

# 결과 출력
print(difference)