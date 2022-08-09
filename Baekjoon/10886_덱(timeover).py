N = int(input())
deq = list()


def push_front(x):
    global deq
    deq = [x] + deq


def push_back(x):
    deq.append(x)


def pop_front():
    global deq
    if not deq:
        return -1
    else:
        rlt = deq[0]
        deq = deq[1:]
        return rlt


def pop_back():
    if not deq:
        return -1
    else:
        rlt = deq.pop()
        return rlt


def size():
    return len(deq)


def empty():
    if not deq:
        return 1
    else:
        return 0


def front():
    if not deq:
        return -1
    else:
        return deq[0]


def back():
    if not deq:
        return -1
    else:
        return deq[-1]


for _ in range(N):
    temp = list(map(str, input().split()))
    if temp[0] == 'push_back':
        push_back(int(temp[1]))
    elif temp[0] == 'push_front':
        push_front(int(temp[1]))
    elif temp[0] == 'pop_front':
        print(pop_front())
    elif temp[0] == 'pop_back':
        print(pop_back())
    elif temp[0] == 'size':
        print(size())
    elif temp[0] == 'empty':
        print(empty())
    elif temp[0] == 'front':
        print(front())
    elif temp[0] == 'back':
        print(back())
        