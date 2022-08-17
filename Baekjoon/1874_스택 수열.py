from sys import stdin
from collections import deque

N = int(stdin.readline())

test = deque()
num = deque([x for x in range(1, N+1)])

for _ in range(N):
    test.append(int(stdin.readline()))

stack = list()
top = 0
answer = list()

while True:
    if not test:
        for a in answer:
            print(a)
        break
    else:
        t = test.popleft()
        if t > top:
            for _ in range(t -top):
                answer.append('+')
                temp = num.popleft()
                stack.append(temp)
            stack.pop()
            answer.append('-')
            top = t
        elif t < top:
            if t != stack[-1]:
                print('NO')
                break
            else:
                stack.pop()
                answer.append('-')

