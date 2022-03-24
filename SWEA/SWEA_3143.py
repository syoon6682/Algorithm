import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    cnt = 0 # 카운트
    i = 0 # 검색하는 위치

    while True:
        if A[i:i+len(B)] == B: # B 문자가 있는 경우
            i += len(B) # B의 길이만큼 검사 포인터 옮기기
            cnt += 1
            if i >= len(A):
                break
        else: # 없는 경우
            i += 1 # 검사 포인터 1 옮기고
            cnt += 1 # 카운트 1 더하기
            if i >= len(A):
                break

    print(f'#{tc} {cnt}')

