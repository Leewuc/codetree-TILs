# 문자열 배열을 구현합니다.
string = []
cnt = 0
	
# 0이 나올때까지 반복합니다.
while True:
	# 문자열을 입력받습니다.
	inp = input()
	string.append(inp)
		
	# 0이 나올 경우 while문을 빠져나옵니다.
	if string[cnt] == "0":
		break
		
	cnt += 1
	
# 문자열의 개수를 출력합니다.
print(cnt)
	
# 홀수 번째 문자열을 출력합니다.
for i in range(0, cnt, 2):
	print(string[i])