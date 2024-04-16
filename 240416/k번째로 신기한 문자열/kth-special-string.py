n, k, start_str = input().split()
n = int(n)
k = int(k)
words = []
for _ in range(n):
    word = input()
    if word.startswith(start_str):
        words.append(word)
words.sort()
print(words[k-1])