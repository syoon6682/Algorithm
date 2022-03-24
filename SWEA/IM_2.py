import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, p = map(int, input().split())
    field_list = [list(map(int, input().split())) for _ in range(N)] # 데이터 입력

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 가로세로 델타
    cross_d = [(1, 1), (1, -1), (-1, -1), (-1, 1)] # 대각선 델타

    def total_sum(x, y, method): # 좌표에서 가로세로 혹은 대각선을 지정 후 더해주는 함수
        temp_sum = field_list[x][y] # 시작점 더하고 시작하면서
        for k in range(1, p+1): # 힘의 정도는 1~p까지 계산해야하니까 반복하고
            for l in range(4): # 4방향이므로 4번 반복하고
                modified_x = x + k * method[l][0] # 해당되는 힘만큼 값을 수정해주는데
                modified_y = y + k * method[l][1]
                if modified_x < 0 or modified_y < 0 or modified_x >= N or modified_y >= N: # 범위를 벗어나면 패스
                    pass
                else: # 안 벗어나면 해당값 temp_sum에 합산
                    temp_sum += field_list[modified_x][modified_y]

        return temp_sum # 반환


    max_sum = 0 # 최대값 담을 변수
    for i in range(N): # x축 순회
        for j in range(N): # y축 순회
            if total_sum(i, j, d) > max_sum: # 계산 결과가 이제까지 중에 가장 크면
                max_sum = total_sum(i, j, d) # 값 갱신
            if total_sum(i, j, cross_d) > max_sum:
                max_sum = total_sum(i, j, cross_d)


    print(f'#{tc} {max_sum}')

