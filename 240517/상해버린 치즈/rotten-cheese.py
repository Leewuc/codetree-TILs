N, M, D, S = map(int, input().split())
cheese_logs = [[] for _ in range(M+1)]  # M+1 크기의 리스트를 생성하여 각 치즈를 먹은 사람과 시간을 저장합니다.
sick_logs = [0] * (N+1)  # N+1 크기의 리스트를 생성하여 각 사람이 언제 아팠는지 저장합니다.

# 치즈를 먹은 기록 처리
for _ in range(D):
    p, m, t = map(int, input().split())
    cheese_logs[m].append((p, t))

# 아픈 기록 처리
for _ in range(S):
    p, t = map(int, input().split())
    sick_logs[p] = t

# 각 치즈별로 확인하여 최대 몇 명이 아플 수 있는지 계산합니다.
max_sick = 0
for m in range(1, M+1):
    possible_sick = 0
    for p, t in cheese_logs[m]:
        if sick_logs[p] == 0 or sick_logs[p] >= t+1:  # 아픈 기록이 없거나, 치즈를 먹은 후 1초 이상 지나서 아프다면
            possible_sick += 1
        elif sick_logs[p] < t+1:  # 아픈 기록이 치즈를 먹은 시간보다 빠르다면, 이 치즈는 상한 치즈가 아님
            possible_sick = 0
            break
    max_sick = max(max_sick, possible_sick)

print(max_sick)