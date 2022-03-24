import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    S = input() # 문자 입력 받기
    stack = []
    for s in S:
        if len(stack) == 0: # stack이 비어있으면 push
            stack.append(s)
        elif s == stack[-1]: # peak과 push할 원소가 같으면 pop
            stack.pop()
        else: # 그 외에는 push
            stack.append(s)

    print(f'#{tc} {len(stack)}') # stack의 길이 출력

