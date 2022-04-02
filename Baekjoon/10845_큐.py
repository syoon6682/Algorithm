N = int(input())
queue = list()
start = -1
end = -1


def push(n):
    global end
    queue.append(n)
    end += 1


def pop():
    global start
    if start == end:
        print(-1)
    else:
        start += 1
        print(start)


def size():
    global start, end
    print(end-start)


def empty():
    global start, end
    if end - start <= 1:
        print(0)
    else:
        print(1)


def front():
    if empty():
        print(-1)
    else:
        print(queue[start+1])


def back():
    if empty():
        print(-1)
    else:
        print(queue[end])


for _ in range(N):
    temp = list(map(str, input().split()))
    if len(temp) > 1:
        push(int(temp[1]))

    elif temp[0] == 'pop':
        front()

    elif temp[0] == 'size':
        size()

    elif temp[0] == 'empty':
        empty()

    elif temp[0] == 'front':
        front()

    elif temp[0] == 'back':
        back()




