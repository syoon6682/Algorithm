N, M = map(int, input().split())
visited = []

def printer(n):
    global N, M, visited

    cnt = 0

    # 전체 숫자 리스트
    num_list = []
    for i in range(N):
        num_list.append(i+1)

    if len(visited) == n:
        # print 찍기
        return
    else:
        for j in num_list:



