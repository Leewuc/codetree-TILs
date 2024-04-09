# 문자와 숫자를 입력받습니다.
x, a = input().split()
a = int(a)
	
# 문자의 아스키코드값과 숫자 아스키코드 번호에 해당하는 문자값을 출력합니다.
print(ord(x), chr(a))