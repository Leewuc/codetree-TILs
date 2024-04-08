arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

v = 0

for i in range (2):
    v = 0
    for j in range(4):
        v += arr[i][j]
    print(f"{v/4:.1f}", end=" ")
print()

for i in range(4):
    v = 0
    for j in range(2):
        v += arr[j][i]
    print(f"{v/2:.1f}", end=" ")
print()

v = 0 

for i in range (2):
    for j in range(4):
        v += arr[i][j]
print(f"{v/8:.1f}")