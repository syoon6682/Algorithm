from collections import deque
from sys import stdin

T = int(stdin.readline())


for _ in range(T):
    p = stdin.readline().strip()
    n = int(stdin.readline())
    l = stdin.readline()

    # 문자열 슬라이싱
    if n != 0:
        list1 = deque(list(l[1:-2].split(',')))
    else:
        list1 = deque()

    # 연산 근데 가지치기를 먼저 곁들인
    cnt = p.count('D')
    reverse_cnt = len(p) - cnt

    if cnt > len(list1):
        print('error')
    else:
        status = True
        s = 0
        e = len(p)
        while True:
            if s == e:
                break
            elif p[s] == 'R':
                if status:
                    status = False
                else:
                    status = True
            elif p[s] == 'D':
                if status:
                    list1.popleft()
                else:
                    list1.pop()

            s += 1

        if reverse_cnt // 2:
            print(list(map(int, list1)))
        else:
            list1.reverse()
            print(list(map(int, list1)))

