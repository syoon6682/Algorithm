import sys

N = int(sys.stdin.readline())

word = list()

for _ in range(N):
    word.append(sys.stdin.readline().strip())

word = list(set(word))

word.sort(key=lambda x:(len(x), x))

for w in word:
    print(w)