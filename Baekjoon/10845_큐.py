import sys

N = int(sys.stdin.readline())
queue = list()
start = -1
end = -1


def push(n):
    global end
    queue.append(n)
    end += 1


def size():
    global start, end
    print(end-start)


def empty():
    global start, end
    if end == start:
        return 1
    else:
        return 0


def front():
    if end == start:
        print(-1)
    else:
        print(queue[start+1])


def back():
    if end == start:
        print(-1)
    else:
        print(queue[end])


def pop():
    global start
    if end == start:
        print(-1)
    else:
        start += 1
        print(queue[start])


for _ in range(N):
    temp = list(map(str, sys.stdin.readline().split()))
    if len(temp) > 1:
        push(int(temp[1]))

    elif temp[0] == 'pop':
        pop()

    elif temp[0] == 'size':
        size()

    elif temp[0] == 'empty':
        print(empty())

    elif temp[0] == 'front':
        front()

    elif temp[0] == 'back':
        back()




