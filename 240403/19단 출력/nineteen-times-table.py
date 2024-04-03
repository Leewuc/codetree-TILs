for i in range(1, 20):
    for j in range(1, 20):
        ## 짝수일때는 줄을 나눠줌 / 19단의 마지막인 19배수를 곱했을 때도 다음에 단을 나눠줌
        if j % 2 == 0 or j == 19:
            print(f"{i} * {j} = {i * j}")
        else:
            print(f"{i} * {j} = {i * j}", end = " / ")