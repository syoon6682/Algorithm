import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 입력받기
    N, M = map(int, input().split())
    num_list = list(map(int,input().split()))

    # M을 N으로 나눈 나머지 인덱스의 숫자가 맨 앞으로 오게 되기 때문에 idx 변수 설정후 인덱싱
    idx = M % N

    print(f'#{tc} {num_list[idx]}') #출력

