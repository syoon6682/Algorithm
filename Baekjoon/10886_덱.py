from collections import deque
import sys

d = deque()

N = int(sys.stdin.readline())

for _ in range(N):
    temp = list(map(str, sys.stdin.readline().strip().split()))
    try:

        if temp[0] == 'push_front':
            d.appendleft(int(temp[1]))

        elif temp[0] == 'push_back':
            d.append(int(temp[1]))

        elif temp[0] == 'pop_front':
            print(d.popleft())

        elif temp[0] == 'pop_back':
            print(d.pop())

        elif temp[0] == 'size':
            print(len(d))

        elif temp[0] == 'empty':
            if len(d) == 0:
                print(1)
            else:
                print(0)

        elif temp[0] == 'front':
            print(d[0])

        elif temp[0] == 'back':
            print(d[-1])

    except IndexError:
        print(-1)