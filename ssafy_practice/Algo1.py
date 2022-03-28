T = int(input())

for tc in range(1, T + 1):

    # 데이터 받기 및 비어있는 farm 2차원 배열 생성
    N, M = map(int, input().split())
    rabbit_list = list(list(map(int, input().split())) for _ in range(M))
    farm = list([0] * N for _ in range(N))

    # 상하좌우 활용을 위한 딕셔너리
    P = {
        0: [-1, 0],
        1: [1, 0],
        2: [0, -1],
        3: [0, 1]
    }

    # 훔치는 위치를 1로 표시하면서 farm에서 훔쳤다고 표현하는 함수
    def robber(x, y, direc, jump):
        farm[x][y] = 1
        while True:
            new_x = x + P[direc][0] * jump
            new_y = y + P[direc][1] * jump
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                break
            else:
                farm[new_x][new_y] = 1
                x = new_x
                y = new_y

    # 토끼가 다 훔친 farm 함수에서 1을 세주는 함수
    def count(rlt):
        cnt = 0
        for i in range(N):
            for j in range(N):
               if rlt[i][j] == 1:
                   cnt += 1
        return cnt

    # 만든 함수 적용
    for r in rabbit_list:
        robber(r[0], r[1], r[2], r[3])

    result = count(farm)

    print(f'#{tc} {result}')

