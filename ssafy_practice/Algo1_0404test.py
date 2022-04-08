T = int(input())

for tc in range(1, T+1):

    # 주어진 데이터를 양식에 맞게 받기
    N, M, K = map(int, input().split())
    lake = list(list(map(int, input().split())) for _ in range(N))
    tot_max = 0

    # 그물로 잡는 함수 catch 생성
    # 기본적인 아이디어는 시작점을 중심으로 시대 반대방향으로 delta를 따라서 더하는 구조
    def catch(x, y, k):

        # 최대값 기록을 위한 global 설정 및 알맞는 delta 설정(이번 델타는 순서도 중요함!)
        global tot_max
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        tot = 0

        # 시작점을 기준으로 시계 반대 방향으로 돌기
        for d in delta:
            for _ in range(k-1):
                x += d[0]
                y += d[1]
                tot += lake[x][y]

        # 만약 현재 합이 global max 보다 크면 대체
        if tot > tot_max:
            tot_max = tot


    # 모든 구간에서 catch 돌려보고 tot_max를 출력해주기
    for i in range(N-K+1):
        for j in range(M-K+1):
            catch(i, j, K)

    print(f'#{tc} {tot_max}')