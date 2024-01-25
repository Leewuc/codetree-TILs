a,b = input().split()
a,b = int(a),int(b)
def print_numbers(a, b):
    while a <= b:
        print(a,end=" ")
        if a % 2 == 1:  # If the number is odd
            a *= 2      # Double the number
        else:                # If the number is even
            a += 3      # Increase the number by 3
    return
print_numbers(a, b)