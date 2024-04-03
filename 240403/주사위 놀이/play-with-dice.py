results = list(map(int, input().split()))

counts = [0] * 6
for result in results:
    counts[result - 1] += 1

for i in range(6):
    print(f"{i + 1} - {counts[i]}")