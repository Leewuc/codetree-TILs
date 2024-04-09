# 문자열을 입력 받습니다.
string = input()

# 'ee'와 'eb'의 개수를 세기 위한 변수를 초기화합니다.
count_ee = 0
count_eb = 0

# 문자열을 순회하면서 'ee'와 'eb'의 개수를 세어줍니다.
for i in range(len(string) - 1):
    if string[i:i+2] == 'ee':
        count_ee += 1
    elif string[i:i+2] == 'eb':
        count_eb += 1

# 결과를 출력합니다.
print(count_ee, count_eb)