# 두 정수를 입력 받습니다.
a, b = map(int, input().split())

# 두 수를 더한 결과를 구하고, 결과에서 숫자 1의 개수를 세어 출력합니다.
result = a + b
count_of_1 = str(result).count('1')
print(count_of_1)