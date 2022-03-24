import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    S = input() # 주어진 식 저장
    postfix = []
    for s in range(1, len(S)-1):
        postfix.append(S[s+1])
        postfix.append(S[s])

    print(f'#{tc} {postfix}')

