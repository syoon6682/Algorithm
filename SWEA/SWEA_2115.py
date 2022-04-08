import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    bee = list(list(map(int, input().split())) for _ in range(N))
    visited = []
    tot_max = 0

    # 인부들의 담당 벌통을 정하는 함수
    def select(idx, m):
        global tot_max
        if idx == 2:
            cal(0, visited)
            return
        else:
            if idx == 0:
                for i in range(N):
                    for j in range(N-m+1):
                        if [i, j] not in visited:
                            visited.append([i, j])
                            select(idx+1, m)
                            visited.pop()
            else:
                temp_list = list()
                for i in range(M):
                    temp_list.append([visited[0][0], visited[0][1]+i])
                for i in range(N):
                    for j in range(N-m+1):
                        if [i, j] not in temp_list:
                            visited.append([i, j])
                            select(idx+1, m)
                            visited.pop()

    # 그 두개의 벌통의 연산값을 구하는 과정...이 되야하지만
    # 목표값이 2개가 발생하는 상황에서 어떻게 마무리를 지어야 하는지 헷갈려서 계속 고민중입니다. 
    def cal(idx, worker):

        for l in worker:
            worker_visit = list()
            if idx == len(worker):
                w_max
                return
            else:
                for w in worker:
                    if w not in worker_visit:
                        worker_visit.append(w)
                        cal(idx+1, worker)
                        worker_visit.pop()


    select(0, M)

    print(f'#{tc} {T}')

