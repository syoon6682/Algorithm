import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    atom = list()
    energy = 0
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        atom.append([2*x, 2*y, d, k])

    direc = {
        0: [0,1],
        1: [0,-1],
        2: [-1, 0],
        3: [1, 0]
    }

    while len(atom) > 0:
        for a in range(len(atom)):
            atom[a][0] += direc[atom[a][2]][0]
            atom[a][1] += direc[atom[a][2]][1]

        delete = list()
        locate = list()
        for a in range(len(atom)):
            before_len = len(locate)
            if [atom[a][0], atom[a][1]] in locate:
                delete.append([atom[a][0], atom[a][1]])
            else:
                locate.append([atom[a][0], atom[a][1]])

        for d in delete:
            for a in atom:
                if d == [a[0], a[1]]:
                    energy += a[3]
                    atom.remove(a)
                elif atom[a][0] > 2000 or atom[a][1] > 2000 or atom[a][0] < -2000 or atom[a][1] < -2000:
                    atom.remove(atom[a])

    print(f'#{tc} {energy}')

