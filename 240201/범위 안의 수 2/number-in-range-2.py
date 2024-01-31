# Initialize variables for sum and count
total_sum = 0
count = 0

# Read 10 integers from input and calculate sum of those between 0 and 200
for _ in range(10):
    num = int(input())
    if 0 <= num <= 200:
        total_sum += num
        count += 1

# Calculate average (rounded to one decimal place)
average = round(total_sum / count, 1)

# Print the sum and average separated by a space
print(total_sum, average)