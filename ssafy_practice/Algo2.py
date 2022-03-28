T = int(input())

for tc in range(1, T + 1):

    # 데이터 받은 후 지나갔는지 확인하는 0으로 초기화 된 N*N visted 2차원 배열과 땅 최대 크기를 저장하는 max_size 함수 정의
    N = int(input())
    ground = list(list(map(int, input().split())) for _ in range(N))
    visited = list([0]*N for _ in range(N))
    max_size = 0

    # 땅의 넓이를 측정하기 위해 bfs 활용
    def bfs(x, y):
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 방향 설정을 위한 델타 설정
        que = [[x, y]] # 한 땅을 기록하기 위한 queue
        start = 0
        end = 1

        visited[x][y] = 1 # visited에 시작점을 기록하고 시작
        while start != end:

            # 델타를 활용하여 네방향 조사
            for d in delta:
                new_x = que[start][0] + d[0]
                new_y = que[start][1] + d[1]

                # 범위를 벗어나면 넘어가기
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
                    continue

                # 만약 판매하는 땅이고 bfs로 방문한 적이 없으면 방문 표시하고 queue에 추가
                elif ground[new_x][new_y] != 0 and visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = 1
                    que.append([new_x, new_y])

            start += 1
            end = len(que)

        # 땅의 가격을 계산하기 위한 과정
        # que에 있는 좌표를 활용해 땅의 가격을 가산함
        price = 0
        for q in que:
            price += ground[q[0]][q[1]]

        return [len(que), price] # [땅의 크기, 땅의 가격] return

    # bfs 함수 적용
    for i in range(N):
        for j in range(N):
            # 판매하는 땅이고 가본 적이 없는 곳이면 bfs 시작점으로 적용
            if ground[i][j] != 0 and visited[i][j] == 0:
                temp = bfs(i, j)

                # 최대 크기보다 크면 무조건 사야하므로 바로 result에 땅의 가격 저장
                if temp[0] > max_size:
                    max_size = temp[0]
                    result = temp[1]

                # 최대 크기랑 같다면 싼 땅을 사야하므로 크기 비교 후 result에 땅의 가격 저장
                elif temp[0] == max_size:
                    if temp[1] < result:
                        result = temp[1]

    print(f'#{tc} {result}')

