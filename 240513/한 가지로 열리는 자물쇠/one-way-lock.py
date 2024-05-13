def count_unlock_combinations(N, combination):
    # 주어진 조합에서 각 자리 숫자를 추출
    a, b, c = combination

    # 자물쇠를 열 수 있는 조합의 수를 저장할 변수
    count = 0

    # 모든 가능한 조합을 생성하기 위한 3중 for 루프
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                # 현재 조합이 주어진 조건을 만족하는지 확인
                # 즉, 최소 한 자리가 주어진 숫자와 거리가 2 이내인지 확인
                if abs(a - i) <= 2 or abs(b - j) <= 2 or abs(c - k) <= 2:
                    count += 1

    # 조건을 만족하지 않는 조합을 제거
    # 총 조합 수에서 조건을 만족하는 조합의 수를 빼줌
    return count

# 입력 예제
N = int(input())
combination = tuple(map(int, input().split()))

# 자물쇠를 열 수 있는 조합의 수를 계산하여 출력
print(count_unlock_combinations(N, combination))