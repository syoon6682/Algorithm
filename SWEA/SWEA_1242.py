import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code_list = list(str(input()) for _ in range(N))
    blank_tester = '0'*M

    def search_code(start):
        for s in range(start, N):
            if code_list[s] != blank_tester:
                return code_list[s]

    def trans_16_to_2(test):
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

        transformed = ''
        for s in test:
            for k in P.keys():  # 대응하는 딕셔너리를 만나면
                if s == k:
                    transformed += P[k]  # 대응하는 value를 더해주기
                    break

        return transformed

    def find_start(start, tester):
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
        for idx in range(start, len(tester)):
            for k in P.keys():
                if k == tester[idx:idx+7]:
                    return idx

    def transform(start, tester):
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
        num_list = list()
        for n in range(8):
            for k in P.keys():
                if k == tester[start+n*7:start+(n+1)*7]:
                    num_list.append(P[k])
                    break

    def judge(tester): # 8자리의 str 입력받기
        for i in range(7):
            pass
        return 0


    test_code = search_code(0)
    test_code = trans_16_to_2(test_code)
    start_point = find_start(0, test_code)

    print(f'#{tc} {start_point}')

