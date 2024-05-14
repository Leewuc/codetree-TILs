def check_count(secret, guess, exact, near):
    exact_count = 0
    near_count = 0
    secret_used = [False] * 3
    guess_used = [False] * 3
    
    # 1번 카운트 확인 (정확히 일치하는 경우)
    for i in range(3):
        if secret[i] == guess[i]:
            exact_count += 1
            secret_used[i] = True
            guess_used[i] = True

    # 2번 카운트 확인 (있지만 위치가 다른 경우)
    for i in range(3):
        if guess_used[i]:
            continue
        for j in range(3):
            if secret[j] == guess[i] and not secret_used[j]:
                near_count += 1
                secret_used[j] = True
                break
    
    return exact_count == exact and near_count == near

def find_possible_answers(N, queries):
    possible_answers = 0

    # 모든 가능한 3자리 숫자를 대상으로 확인
    for i in range(1, 10):
        for j in range(1, 10):
            if j == i:
                continue
            for k in range(1, 10):
                if k == i or k == j:
                    continue
                secret = [i, j, k]
                all_match = True
                
                # 모든 쿼리에 대해 조건을 만족하는지 확인
                for guess, exact, near in queries:
                    if not check_count(secret, guess, exact, near):
                        all_match = False
                        break
                
                if all_match:
                    possible_answers += 1
    
    return possible_answers

N = int(input())
queries = []
for _ in range(N):
    guess_str, exact, near = input().split()
    guess = list(map(int, list(guess_str)))
    queries.append((guess, int(exact), int(near)))

print(find_possible_answers(N, queries))