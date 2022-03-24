import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    num_list = list(input().split())
    stack = []
    for s in num_list:
        try: # 에러가 안뜨는 상황에서
            if s.isdecimal(): # 숫자면 stack에 추가
                stack.append(int(s))
            elif s == '+': # + 일때
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append((num1+num2))
            elif s == '-': # - 일때
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append((num2-num1))
            elif s == '*': # * 일때
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append((num1*num2))
            elif s == '/': # / 일때
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append((num2//num1))

            elif s == '.':
                if len(stack) != 1: # 마지막까지 왔는데 stack에 1개가 아닌 다른 개수가 들어있으면 연산이 잘못됨
                    print(f'#{tc} error')
                else: # 연산이 정상적으로 끝났을 경우
                    result = stack.pop()
                    print(f'#{tc} {result}')

        except: # 에러가 뜨면 에러 출력
            print(f'#{tc} error')
            break


