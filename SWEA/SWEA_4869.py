"""
규칙성을 찾다보니
짝수번째는 직전 횟수의 *2 +1,
홀수번째는 직전 횟수의 *2 -1,
이런 규칙이 나와서 일단은 이렇게 짰습니다..
+ DP
"""

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    N = N // 10 # 10의 배수로 주어진 N을 횟수로 변환
    memo = [1] # 가로가 10일때의 값은 default로 넣어줌
    for i in range(2, N+1):
        if i % 2 == 0: # 짝수면 직전에서 *2+1
            memo.append(memo[-1] * 2 + 1)

        else: # 홀수면 직전에서 *2-1
            memo.append(memo[-1] * 2 - 1)

    print(f'#{tc} {memo[-1]}') # 출력력
