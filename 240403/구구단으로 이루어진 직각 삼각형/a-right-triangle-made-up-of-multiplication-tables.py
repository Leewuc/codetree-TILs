n = int(input())  # n 입력 받기

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(f"{i} * {j} = {i * j}",end="")
        if j == (n-i+1):
            print("",end="")
        else:
            print("",end=" / ")
    print()