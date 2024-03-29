def check_multiple_of_3(numbers):
    for number in numbers:
        if number % 3 != 0:
            return 0
    return 1

# 입력
numbers = [int(input()) for _ in range(5)]

# 출력
print(check_multiple_of_3(numbers))