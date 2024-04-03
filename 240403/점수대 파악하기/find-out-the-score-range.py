counts = [0] * 11  # 10점 단위로 구분하기 위해 11개의 구간으로 나눔
scores = list(map(int, input().split()))

for score in scores:
    if score == 0:
        break
    tens_digit = score // 10
    counts[tens_digit] += 1

for i in range(10, 0, -1):
    print(f"{i}0 - {counts[i]}")