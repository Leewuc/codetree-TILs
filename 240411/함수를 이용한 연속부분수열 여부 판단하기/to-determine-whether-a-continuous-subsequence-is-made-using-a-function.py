def is_subsequence(a, b):
    # Convert the lists to strings for easy comparison
    a_str = ' '.join(map(str, a))
    b_str = ' '.join(map(str, b))

    # Check if b_str is a substring of a_str
    if b_str in a_str:
        return "Yes"
    else:
        return "No"

# Read input
n1, n2 = map(int, input().split())
sequence_a = list(map(int, input().split()))
sequence_b = list(map(int, input().split()))

# Check if sequence_b is a subsequence of sequence_a
result = is_subsequence(sequence_a, sequence_b)
print(result)