N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

# 각 폭탄 번호가 나타나는 위치를 저장
bomb_positions = {}
for i, bomb in enumerate(bombs):
    if bomb in bomb_positions:
        bomb_positions[bomb].append(i)
    else:
        bomb_positions[bomb] = [i]

max_bomb_number = -1
for bomb_number, positions in bomb_positions.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if abs(positions[i] - positions[j]) <= K:
                max_bomb_number = max(max_bomb_number, bomb_number)
                break

print(max_bomb_number)