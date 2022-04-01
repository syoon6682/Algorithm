import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    list1_visited = list()

    # 이진탐색하는 함수
    def binary(start, end, target, visit, direction): # (시작점, 끝점, key값, visited 함수, 왼쪽오른쪽 판단)

        # start가 크면 함수 종료
        if start > end:
            return

        # 범위 안에 key 값이 없으면 함수 종료
        if target < list1[start] or target > list1[end]:
            return

        # pivot 설정 후 key값과 같으면 visited에 기록
        pivot = (start+end) // 2
        if list1[pivot] == target:
            visit.append(target)
            return

        # 전방향이 오른쪽이었으면 왼쪽, 왼쪽이었으면 오른쪽 검사하기
        if direction == 'right':
            binary(start, pivot-1, target, visit, 'left')
        elif direction == 'left':
            binary(pivot+1, end, target, visit, 'right')

    # binary 함수를 돌려보는데 만약 처음 방향 오른쪽일때 없으면 처음 방향 왼쪽도 진행해보기
    for i in list2:
        binary(0, N-1, i, list1_visited, 'right')
        if i not in list1_visited:
            binary(0, N-1, i, list1_visited, 'left')

    print(f'#{tc} {len(list1_visited)}')
