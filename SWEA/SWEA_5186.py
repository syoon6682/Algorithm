import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    num = 0
    result = ''
    for i in range(1, 13):                          # 12번 이내로 시도
        if N >= num + 1/(2 ** i) and num < N:       # 만약 2의 -i 승이 가산 가능한 경우
            num += 1/(2 ** i)
            result += '1'
        elif num < N <= num + 1/(2 ** i):           # 만약 2의 -i승이 가산이 불가능한 경우
            result += '0'

        if N == num:                                # 해당값을 찾으면 루프 나오기
            break
    else:                                           # 시도 내에 못찾을 경우 overflow출력
        result = 'overflow'

    print(f'#{tc} {result}')

