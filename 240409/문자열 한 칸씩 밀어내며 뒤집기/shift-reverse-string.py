string, n = input().split()
q = int(n)

for _ in range(q):
    # 문제 인식
    quest = int(input())

    # 문제 수에 따른 처리 
    if quest == 1:
        string = string[1:] + string[0]
    elif quest == 2:
        string = string[-1] + string[:-1]
    else:
        string = string[::-1]

    # 출력
    print(string)