n, q = map(int, input().split())
elements = list(map(int, input().split()))

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        idx = int(query[1]) - 1
        print(elements[idx])
    elif query[0] == '2':
        value = int(query[1])
        idx = next((i for i, x in enumerate(elements) if x == value), 0)
        print(idx + 1)
    elif query[0] == '3':
        start = int(query[1]) - 1
        end = int(query[2])
        print(*elements[start:end])