# 입력 받기
n = int(input())
students = []
for i in range(n):
    height, weight = map(int, input().split())
    students.append((height, weight, i + 1))  # 번호는 1부터 시작

# 정렬하기
students.sort(key=lambda x: (x[0], -x[1]))  # 키는 오름차순, 몸무게는 내림차순 정렬

# 출력하기
for student in students:
    print(student[0], student[1], student[2])