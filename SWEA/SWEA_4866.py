import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    S = input()
    stack = []
    result = 0  # default 상태를 False로 설정
    for s in S:  # 문자열 순회
        if s == '(' or s == '{' or s == '[':  # 만약 열리는 괄호면
            stack.append(s)  # 스택 추가
        elif s == ')':  # 닫히는 괄호라면 break
            if len(stack) == 0: # 닫히는 괄호가 나왔는데 stack이 비어있으면 break
                break
            popped = stack.pop()
            if popped != '(':
                break

        elif s == '}':
            if len(stack) == 0:
                break
            popped = stack.pop()
            if popped != '{':
                break

    else:  # 만약 순회를 다하면 result를 True로 바꿈
        result = 1

    if len(stack) != 0: # 순회를 다 했는데도 stack에 남아있으면 다시 False로 설정
        result = 0

    print(f'#{tc} {result}') #출력

