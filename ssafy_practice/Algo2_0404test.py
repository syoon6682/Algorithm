T = int(input())

for tc in range(1, T+1):

    # 양식에 맞게 데이터 받아주기
    # tot_min은 초기값으로 매우 큰 수를 설정해준 것이고
    # maze는 split 형태로 데이터가 주어진 것이 아니므로 먼저 문자로 받은 후 떨어트려서 데이터를 받았습니다.
    N = int(input())
    maze = list()
    tot_min = 1000000000
    for _ in range(N):
        temp = input()
        temp_list = list()
        for sr in temp:
            temp_list.append(int(sr))
        maze.append(temp_list)

    # 시작점, 끝점, 벽 좌표 다 찾기
    wall = list()
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1:
                wall.append([i, j])
            elif maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                end = [i, j]

    visited = list()

    # DFS를 활용한 벽을 없애는 경우의 수 다 찾기
    def break_wall():

        # 종료 조건
        if len(visited) == 2:
            change_maze(visited)
            return

        # visited가 비어있을 때는 순서대로 wall의 원소 넣기
        # 하나가 있을 때에는 중복 연산을 피하기 위해 그 뒤에 있는 원소를 넣기
        else:
            if len(visited) == 0:
                for w in wall:
                    visited.append(w)
                    break_wall()
                    visited.pop()
            elif len(visited) == 1:
                s = wall.index(visited[0])
                if s < len(wall):
                    for w in range(s+1, len(wall)):
                        visited.append(wall[w])
                        break_wall()
                        visited.pop()

    def change_maze(change):

        # break_wall에서 정한 없앨 벽을 반영
        for c in change:
            maze[c[0]][c[1]] = 0
        BFS(start, maze)

        # 이때 import가 불가하므로 deepcopy가 어려워서 반영한 벽을 원상 복구시키는 로직을 넣어줌
        for c in change:
            maze[c[0]][c[1]] = 1


    # BFS를 활용하여 시작점에서 출발하여 끝점 찾기
    def BFS(s, maz):

        # BFS에 필요한 요소들 먼저 준비
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        que = list()
        q_start = 0
        q_end = 1
        que.append(s)
        que_visit = [s]

        cnt = 0
        while q_start < q_end:
            cnt += 1
            for q in range(q_start, q_end):
                for d in delta:
                    qx = que[q][0] + d[0]
                    qy = que[q][1] + d[1]

                    # qx, qy가 범위를 벗어나면 넘어가기
                    if qx >= N or qx < 0 or qy >= N or qy < 0:
                        continue

                    # qx, qy가 방문한 적 있는 좌표면 넘어가기
                    elif [qx, qy] in que_visit:
                        continue

                    # 좌표가 0이면 진행한 다음 visited 기록하기
                    elif maz[qx][qy] == 0:
                        que.append([qx, qy])
                        que_visit.append([qx, qy])

                    # 도착지에 도착하면 cnt를 기반으로 find_min함수 실행
                    elif maz[qx][qy] == 3:
                        return find_min(cnt)

            #다음 시작점과 끝점 설정해주기
            q_start = q_end
            q_end = len(que)

        return

    # 가장 작은 경로를 출력해주는 함수
    # 만약 지금 나온 cnt 값이 가장 작으면 tot_min값 갱신
    def find_min(tot):
        global tot_min
        if tot < tot_min:
            tot_min = tot


    break_wall() # 함수 실행
    tot_min += 1 # 이때 거리를 재는 방식이 1~4 사이를 4로 보는, 즉, 뺄셈 후 1을 가산하는 방식이므로 1을 더해줌
    if tot_min == 1000000001: # 근데 이제까지 tot_min이 갱신된 적이 없다면 도착한 적이 없는 것이므로
        tot_min = -1 # tot_min은 -1 반환

    print(f'#{tc} {tot_min}')