import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):

    # 데이터 입력
    N = int(input())
    S = input()

    # 후위계산식 만들기
    postfix = ''
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        elif s.isdecimal():
            postfix += s
        elif s == '+' or s == '*':
            stack.append(s)
        elif s == ')':
            popped = ''
            while popped != '(':
                popped = stack.pop()
                if popped != '(':
                    postfix += popped

    while len(stack) > 0:
        postfix += stack.pop()
    print(postfix)
    # 계산 시작
    stack = []
    for s in postfix:
        if s.isdecimal():
            stack.append(int(s))
        elif s == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif s == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)

    print(stack)

    print(f'#{tc} {stack.pop()}')

