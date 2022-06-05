N = int(input())

dynamic = [0, 1, 2, 4]

for i in range(4, 11):
    dynamic += [dynamic[i-3] + dynamic[i-2] + dynamic[i-1]]

for _ in range(N):
    print(dynamic[int(input())])