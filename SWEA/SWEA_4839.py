import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    num_list = [i for i in range(N+1)] # 데이터 입력 받기

    # 이진분류 정의 함수 생성
    def binarySearch(key):
        start = 1 # 시작페이지
        end = N # 끝 페이지
        cnt = 0 # 횟수 체크용 함수
        while start <= end: # 이진 분류 구성
            middle = int((start + end) / 2)
            if num_list[middle] == key:
                return cnt + 1

            elif num_list[middle] > key:
                end = middle
                cnt += 1

            else:
                start = middle
                cnt += 1


    if binarySearch(A) > binarySearch(B):
        print(f'#{tc} B')

    elif binarySearch(A) == binarySearch(B):
        print(f'#{tc} 0')

    else:
        print(f'#{tc} A')



