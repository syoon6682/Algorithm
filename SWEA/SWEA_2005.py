import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    memo = [] # 메모에 활용될 글로벌 변수

    def pascal(n):

        global memo

        # 삼각형의 첫번째와 두번째는 미리 정의 후 memo에 기록
        if n == 1:
            memo.append([1])

        elif n == 2:
            memo.append([1, 1])

        # memo에 마지막에 기록된 list를 기준으로 새로 작성 후 기록
        else:
            temp = []
            temp.append(1) # 처음은 1로 시작하므로 1 추가
            # 직전 list의 0번째부터 마지막 전까지 순회
            # 마지막이 포함될 경우, Indexerror가 나오므로
            for start in range(0, len(memo[-1])-1):
                temp.append(memo[-1][start] + memo[-1][start+1]) # 순회 대상과 그 다음 대상의 합을 temp에 저장
            temp.append(1) # 마지막은 1이므로 1 추가
            memo.append(temp) # 이렇게 만들어진 list를 memo에 추가

    # 만든 pascal 함수를 활용하여 원하는 층까지 쌓기
    for i in range(1, N+1):
        pascal(i)

    # 출력과정
    print(f'#{tc} ')
    for i in memo:
        for j in i:
            print(j, end=' ')
        print('')



