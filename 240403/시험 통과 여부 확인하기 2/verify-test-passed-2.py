n = int(input())
grade_2 = []
cnt = 0

for i in range(n):
    grade = list(map(int, input().split()))
    grade_2.append(grade)

for i in range(n):
    if sum(grade_2[i]) / 4>= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')
print(cnt)