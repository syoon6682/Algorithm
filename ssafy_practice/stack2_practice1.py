N = int(input())

for tc in range(1, N+1):
    stack = []
    S = input()
    print(f'#{tc} ', end='')
    for s in S:
        if s == '(' or s == '+' or s == '-' or s == '*' or s == '/': # 연산자일때는 stack에 추가
            stack.append(s)

        elif s == ')': # 닫는 괄호가 나오면 여는 괄호 나올때까지 pop 후 print
            temp_str = ''
            while True:
                temp_str = stack.pop()
                if temp_str == '(':
                    break
                else:
                    print(temp_str, end='')
        else: # 숫자면 바로 프린트
            print(s, end='')

    while len(stack) > 0: # 순회를 다하고 stack에 남은 연산자는 출력해주기
        print(stack.pop(), end='')

    print('') # 줄바꿈을 위한 print


