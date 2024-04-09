n, A = input().split()  # 정수 n과 문자열 A를 입력 받습니다.
count = 0  # A와 일치하는 문자열의 개수를 저장할 변수를 초기화합니다.

for _ in range(int(n)):  # n번 반복하며
    string = input()  # 문자열을 입력 받습니다.
    if string == A:  # 입력 받은 문자열이 A와 일치하면
        count += 1  # count를 1 증가시킵니다.

print(count)  # A와 일치하는 문자열의 개수를 출력합니다.