import sys

sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)] # 데이터 받기

    for i in range(100):
        if num_list[0][i] == 1: # 첫줄이 1로 시작하면 시작 포인트로 잡고 내려가기 시작
            x, y = 0, i # 포인트값
            direction = 'down'  # 시작 방향은 무조건 아래이므로 down으로 시작
            while True:
                # 우측 끝에 없고 우측에 1이 있으며 그 전 진행 방향이 아래 혹은 오른쪽 일때,
                if y < 99 and num_list[x][y+1] == 1 and (direction == 'down' or direction == 'right'):
                    y += 1
                    direction = 'right'

                # 좌측 끝에 없고 좌측에 1이 있으며 그 전 진행 방향이 아래 혹은 왼쪽 일때,
                elif y > 0 and num_list[x][y-1] == 1 and (direction == 'down' or direction == 'left'):
                    y -= 1
                    direction = 'left'

                # 사다리 끝에 도달했는데 그 값이 2일때 (당첨일 때)
                elif x == 99 and num_list[x][y] == 2:
                    print(f'#{tc} {i}')
                    break

                #사다리 끝에 도달했지만 2가 아닐 때,
                elif x == 99:
                    break

                # 이외의 경우는 아래로 한칸 내려감
                else:
                    x += 1
                    direction = 'down'

        else:
            pass




