def is_interesting(number):
    str_num = str(number)
    digit_count = {}
    
    for digit in str_num:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    
    counts = list(digit_count.values())
    
    if len(counts) == 2:
        counts.sort()
        if counts[0] == 1 and counts[1] > 1:
            return True
    
    return False

def count_interesting_numbers(X, Y):
    count = 0
    
    for number in range(X, Y + 1):
        if is_interesting(number):
            count += 1
    
    return count

# Input
X, Y = map(int, input().split())

# Count and print the number of interesting numbers
result = count_interesting_numbers(X, Y)
print(result)