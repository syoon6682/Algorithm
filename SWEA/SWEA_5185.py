import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    #주어진 데이터 입력받기
    N, M = map(str, input().split())

    # 16진수에 대응하는 2진수 딕셔너리
    P = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    result = ''
    for s in M: # 주어진 16진수가
        for k in P.keys(): # 대응하는 딕셔너리를 만나면
            if s == k:
                result += P[k] # 대응하는 value를 더해주기
                break

    print(f'#{tc} {result}')

