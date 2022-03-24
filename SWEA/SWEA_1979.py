import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())

    num_list = []
    for _ in range(N):
        temp_list = list(map(int, input().split()))
        temp_list.append(0)
        num_list.append(temp_list)

    num_list.append([0]*(N+1))
    total_count = 0
    # 가로
    for i in range(len(num_list)):

        j = 0
        while j < len(num_list):
            if num_list[i][j] == 1:
                cnt = 0
                while num_list[i][j] == 1:
                    cnt += 1
                    j += 1
                if cnt == K:
                    total_count += 1
            else:
                j += 1
    # 전치
    for i in range(N):
        for j in range(N):
            if i > j:
                num_list[i][j], num_list[j][i] = num_list[j][i], num_list[i][j]


    #세로
    for i in range(len(num_list)):
        j = 0
        while j < len(num_list):
            if num_list[i][j] == 1:
                cnt = 0
                while num_list[i][j] == 1:
                    cnt += 1
                    j += 1
                if cnt == K:
                    total_count += 1
            else:
                j += 1

    print(f'#{tc} {total_count}')

