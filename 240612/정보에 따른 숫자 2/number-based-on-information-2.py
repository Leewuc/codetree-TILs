def find_special_positions(T, a, b, letters_positions):
    S_positions = []
    N_positions = []

    for letter, pos in letters_positions:
        if letter == 'S':
            S_positions.append(pos)
        elif letter == 'N':
            N_positions.append(pos)

    def nearest_distance(positions, x):
        return min(abs(p - x) for p in positions)

    special_count = 0

    for x in range(a, b + 1):
        d1 = nearest_distance(S_positions, x)
        d2 = nearest_distance(N_positions, x)
        if d1 <= d2:
            special_count += 1

    return special_count

# Read input
T, a, b = map(int, input().strip().split())
letters_positions = [input().strip().split() for _ in range(T)]
letters_positions = [(c, int(x)) for c, x in letters_positions]

# Find and print the number of special positions
print(find_special_positions(T, a, b, letters_positions))