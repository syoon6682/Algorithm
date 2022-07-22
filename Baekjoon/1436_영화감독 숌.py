N = int(input())


def tester(n):
    n = str(n)
    for i in range(0, len(n)-2):
        if n[i] == '6' and n[i+1] == '6' and n[i+2] == '6':
            return 1

    return 0


num = 666
movie = list()

tester(num)

while True:
    if N == len(movie):
        print(movie[N-1])
        break
    else:
        if tester(num) == 1:
            movie.append(num)
        num += 1
