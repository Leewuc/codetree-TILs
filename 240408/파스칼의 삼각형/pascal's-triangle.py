def print_pattern(n):
    for i in range(n):
        coef = 1
        for j in range(1, i+2):
            print(coef, end=" ")
            coef = coef * (i + 1 - j) // j
        print()

print_pattern(6)