# 입력 문자열을 받습니다.
input_str = input()

# 목적 문자열을 받습니다.
target_str = input()

# 목적 문자열이 부분 문자열로 존재하는 경우, 가장 앞선 인덱스를 출력합니다.
# 존재하지 않는 경우 -1을 출력합니다.
if target_str in input_str:
    print(input_str.index(target_str))
else:
    print(-1)