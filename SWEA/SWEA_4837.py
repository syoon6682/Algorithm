import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, k = map(int, input().split())
    A = [i for i in range(1, 13)]
    cnt = 0

    for i in range(1 << len(A)):
        temp_list = []
        for j in range(len(A)):
            if i & (1 << j):
                temp_list.append(A[j]) # 부분 집합 구하기
        if len(temp_list) == N: # 부분 집합 크기가 주어진 크기와 같다면
            temp_sum = 0
            for s in temp_list: # 그 합을 다 구해보는데
                temp_sum += s
            if temp_sum == k: # 그 합이 원하는 답과 같다면
                cnt += 1 # cnt를 1 증가시킴

    print(f'#{tc} {cnt}')

