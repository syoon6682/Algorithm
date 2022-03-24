import sys

sys.stdin = open('input.txt')


T = int(input())


# 사칙연산 함수
def cal(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a // b


for test_case in range(1, T + 1):
    lst = list(input().split())
    stack = []
    isError = False

    # 입력을 한 글자씩 순회
    for letter in lst:
        # 에러거나 마침표면 반복 종료
        if isError or letter == '.': break
        # 숫자면 스택에 추가
        if letter.isdigit():
            stack.append(int(letter))
        # 연산자일때
        else:
            # 스택에 숫자가 1개 이하면 에러
            if len(stack) <= 1:
                isError = True
            # 스택에 숫자가 2개 이상이면 연산 후 다시 스택에 넣기
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(cal(first, second, letter))

    # 연산이 끝나고 스택의 길이가 2 이상이면 에러
    if len(stack) != 1:
        isError = True

    if isError:
        print(f'#{test_case} error')
    else:
        print(f'#{test_case} {stack[0]}')