N, M = map(int, input().split())

tet = list()
for _ in range(N):
    temp = list(map(int, input().split()))
    tet.append(temp)

global_sol = 0


def solution(l):
    global global_sol

    if l > global_sol:
        global_sol = l


# 이때 s는 x, y 좌표를 가진 배열로 들어감
def brute(s):
    x = s[0]
    y = s[1]
    # 2, 1, 8, 4, 4 = 19

    # case 1: 긴거
    if y+3 < M:
        local = tet[x][y] + tet[x][y+1] + tet[x][y+2] + tet[x][y+3]
        solution(local)
    if x+3 < N:
        local = tet[x][y] + tet[x+1][y] + tet[x+2][y] + tet[x+3][y]
        solution(local)

    # case 2: 네모난거
    if x+1 < N and y+1 < M:
        local = tet[x][y] + tet[x][y+1] + tet[x+1][y] + tet[x+1][y+1]
        solution(local)

    # case 3: 갈고리
    if x+2 < N and y+1 < M:
        local = tet[x][y] + tet[x+1][y] + tet[x+2][y] + tet[x+2][y+1]
        solution(local)

    if x+2 < N and y-1 >= 0:
        local = tet[x][y] + tet[x+1][y] + tet[x+2][y] + tet[x+2][y-1]
        solution(local)

    if x+1 < N and y+2 < M:
        local = tet[x][y] + tet[x+1][y] + tet[x+1][y+1] + tet[x+1][y+2]
        solution(local)

    if x+1 < N and y-2 >= 0:
        local = tet[x][y] + tet[x+1][y] + tet[x+1][y-1] + tet[x+1][y-2]
        solution(local)

    if x-1 >= 0 and y+2 < M:
        local = tet[x][y] + tet[x-1][y] + tet[x-1][y+1] + tet[x-1][y+2]
        solution(local)

    if x-1 >= 0 and y-2 >= 0:
        local = tet[x][y] + tet[x-1][y] + tet[x-1][y-1] + tet[x-1][y-2]
        solution(local)

    if x-2 >= 0 and y+1 < M:
        local = tet[x][y] + tet[x-1][y] + tet[x-2][y] + tet[x-2][y+1]
        solution(local)

    if x-2 >= 0 and y-1 >= 0:
        local = tet[x][y] + tet[x-1][y] + tet[x-2][y] + tet[x-2][y-1]
        solution(local)

    # case 4: 울퉁불퉁
    if x+1 < N and y+2 < M:
        local = tet[x][y] + tet[x][y+1] + tet[x+1][y+1] + tet[x+1][y+2]
        solution(local)

    if x+1 < N and y-2 >= 0:
        local = tet[x][y] + tet[x][y-1] + tet[x+1][y-1] + tet[x+1][y-2]
        solution(local)

    if x+2 < N and y+1 < M:
        local = tet[x][y] + tet[x+1][y] + tet[x+1][y+1] + tet[x+2][y+1]
        solution(local)

    if x+2 < N and y-1 >= 0:
        local = tet[x][y] + tet[x+1][y] + tet[x+1][y-1] + tet[x+2][y-1]
        solution(local)


    # case 5: ㅗ
    if x+1 < N and y+2 < M:
        local = tet[x][y] + tet[x][y+1] + tet[x+1][y+1] + tet[x][y+2]
        solution(local)

    if x-1 >= 0 and y + 2 < M:
        local = tet[x][y] + tet[x][y+1] + tet[x-1][y+1] + tet[x][y+2]
        solution(local)

    if x+2 < N and y+1 < M:
        local = tet[x][y] + tet[x+1][y] + tet[x+1][y+1] + tet[x+2][y]
        solution(local)

    if x+2 < N and y-1 >= 0:
        local = tet[x][y] + tet[x+1][y] + tet[x+1][y-1] + tet[x+2][y]
        solution(local)


# brute 적용
for n in range(N):
    for m in range(M):
        brute([n, m])

print(global_sol)
