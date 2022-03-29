import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # 데이터를 받고 배달된 항목을 저장하는 delvered list 생성
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    deliver = list(map(int, input().split()))
    delivered = list()

    # 저장된 화물을 다 검사해보기
    while len(weight) != 0:
        temp = max(weight)                      # 가장 무거운 거부터 검사 진행
        if temp > max(deliver):                 # 해당 화물이 운송 최대량보다 크면 검사 안하고 pass
            weight.remove(temp)                 # weight에서 지워버리는 걸로 검사 완료 표현
            continue
        possible = list()                       # 여기다가 가능한 트럭들을 기록
        for i in deliver:                       # 가능한 트럭을 찾는 반복문
            if i >= temp:
                possible.append(i)
        min_poss = min(possible)                # 가능한 트럭 중 가장 작은 트럭 선택
        min_index = deliver.index(min_poss)     # 실은 트럭은 0으로 초기화 하고 delivered에 추가하고 검사 완료
        deliver[min_index] = 0
        delivered.append(temp)
        weight.remove(temp)

    print(f'#{tc} {sum(delivered)}')

