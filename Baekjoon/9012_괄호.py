N = int(input())

for _ in range(N):
    S = input()
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if len(stack) == 0:
                print('NO')
                break
            stack.pop()
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')