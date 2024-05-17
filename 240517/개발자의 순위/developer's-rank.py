def count_consistent_pairs(K, N, rankings):
    # a가 b보다 더 높은 순위였던 모든 쌍 (a, b)를 저장
    consistent_pairs = set()

    # 각 쌍 (a, b)에 대해 a가 항상 b보다 높은 순위였는지 확인
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                always_higher = True
                for ranking in rankings:
                    if ranking.index(i) > ranking.index(j):
                        always_higher = False
                        break
                if always_higher:
                    consistent_pairs.add((i, j))

    # 결과 출력
    return len(consistent_pairs)

# 입력
K, N = map(int, input().split())
rankings = [list(map(int, input().split())) for _ in range(K)]

# 결과 계산 및 출력
result = count_consistent_pairs(K, N, rankings)
print(result)