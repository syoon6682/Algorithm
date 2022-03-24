import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    # 상하좌우를 판단하여 겹치는 넓이를 구하는 함수 작성
    def cal_size(list1, list2):
        if list1[0] - list2[0] > 0:
            left = list1[0]
        else:
            left = list2[0]

        if list1[2] - list2[2] > 0:
            right = list2[2]
        else:
            right = list1[2]

        if right < left: # 왼쪽이 오른쪽보다 크면 가로축으로 겹치지 않으므로 0 return
            return 0

        if list1[1] - list2[1] > 0:
            up = list1[1]
        else:
            up = list2[1]

        if list1[3] - list2[3] > 0:
            down = list2[3]
        else:
            down = list1[3]

        if up > down: # 위쪽이 아래쪽보다 크면 세로축으로 겹치지 않으므로 0 return
            return 0
        else:
            return ((right - left + 1) * (down -up + 1))

    # 데이터 받기
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    total_sum = 0

    # num_list의 집합 중 2개인 부분 집합을 구성
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i][4] != num_list[j][4]: # 만약 두 요소가 서로 색이 다르면 넓이 함수 적용
                total_sum += cal_size(num_list[i], num_list[j])

    print(f'#{tc} {total_sum}')

