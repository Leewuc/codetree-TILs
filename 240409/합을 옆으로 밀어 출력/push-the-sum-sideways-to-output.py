n = int(input())  # 수의 개수를 입력 받습니다.
total = sum([int(input()) for _ in range(n)])  # n개의 수를 입력 받아 합을 계산합니다.
total = str(total)
total = total[1:] + total[0]
print(total)  # 합을 좌측으로 한 칸 민 후 출력합니다.