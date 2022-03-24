import sys

sys.stdin = open('input.txt')

T = int(input())

'''
기본적인 아이디어는 행 합과 열 합을 다 구한 후에
부분 행 합과 부분 열 합이 각각 반으로 나누어지면
4등분이 된다는 성질을 활용했습니다. 
'''

for tc in range(1, T + 1):
    N = int(input())
    berry_list = [list(map(int, input().split())) for _ in range(N)] # 데이터 입력

    # 행 합
    row_sum_list = []
    for i in range(N):
        row_sum_list.append(sum(berry_list[i]))

    # 전체 합
    total_sum = sum(row_sum_list)

    # 전치 후 col_sum 구하기
    for i in range(N):
        for j in range(N):
            if i > j:
                berry_list[i][j], berry_list[j][i] = berry_list[j][i], berry_list[i][j]

    col_sum_list = []
    for i in range(N):
        col_sum_list.append(sum(berry_list[i]))

    # 검증단계
    # result는 1로 시작하며 조건을 만족하지 못하면 *0
    # 조건을 만족하면 *1을 해줍니다.
    result = 1

    # 애초에 4의 배수가 아니면 성립이 안됨
    if total_sum % 4 != 0:
        result *= 0

    # 열이 반으로 나누어지는지
    # 처음 열들의 합부터 더해나가면서 전체 합의 절반이 되면 1 반환
    # 절반이 되지 못하고 넘으면 0 반환
    # 미달이면 계속 더하기
    for i in range(N):
        temp_sum = 0
        if temp_sum < total_sum // 2:
            temp_sum += row_sum_list[i]
        elif temp_sum == total_sum // 2:
            result *= 1
            break
        else:
            result *= 0
            break

    # 열과 같은 원리로 행 전개
    for i in range(N):
        temp_sum = 0
        if temp_sum < total_sum // 2:
            temp_sum += col_sum_list[i]
        elif temp_sum == total_sum // 2:
            result *= 1
            break
        else:
            result *= 0
            break


    print(f'#{tc} {result}')

