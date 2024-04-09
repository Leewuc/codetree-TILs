# 문자열을 구현하여 입력받습니다.
string = input()
ans = 0

# 문자열을 순회하여 숫자들만 골라 더해줍니다.
for elem in string:
    if ord(elem) >= ord('0') and ord(elem) <= ord('9'):
        ans += ord(elem) - ord('0')

# 출력
print(ans)