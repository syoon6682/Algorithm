import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    want_list = list(map(int, input().split())) # 만들려고 하는 리스트
    want_list.insert(0, 0) # 1번째 전구가 1번 인덱스로 오게 하기 위해서 맨 앞에 0 추가
    now_list = [0] * (N+1) # want_list로 만들 초기 다 꺼져있는 전구들
    cnt = 0

    def switch(point): # 스위치로 불 바꿈
        if now_list[point] == 1:
            now_list[point] = 0
        else:
            now_list[point] = 1

    for i in range(1, N+1): # now_list 전구를 다 순회할건데
        if want_list[i] != now_list[i]: # i번째가 다르면
            j = 1
            while j*i <= N: # i배수를 범위만큼
                switch(j*i) # 다 전구 스위치를 바꿀거임
                j += 1
            cnt += 1 # 그리고 카운트 1

    print(f'#{tc} {cnt}') # 출력