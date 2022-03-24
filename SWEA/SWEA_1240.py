import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    blank_tester = '0' * M

    P = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    tester = ''
    for _ in range(N):
        line = input()
        if line != blank_tester:
            tester = line

    # 시작점 찾는 함수
    def find_start(start):
        for s in range(start, len(tester)):
            for n in P.keys():
                if n == tester[s:s+7]:
                    start_point = s
                    return start_point

    # 시작점을 기준으로 숫자 변환하는 함수
    def transform(start):
        num_list = list()
        for n in range(8):
            for k in P.keys():
                if k == tester[start+n*7:start+(n+1)*7]:
                    num_list.append(P[k])
                    break
            else: # 만약에 맞지 않는 코드면 시작점 다시 찾기
                return transform(find_start(start+1))

        return num_list

    # 정상 암호 검정
    result_list = transform(find_start(0))
    check = 0
    for i in range(7):
        if i%2 == 0:
            check += result_list[i]*3
        else:
            check += result_list[i]

    if (check + result_list[7]) % 10 == 0:
        result = sum(result_list)
    else:
        result = 0

    print(f'#{tc} {result}')

