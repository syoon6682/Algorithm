import sys

N = int(sys.stdin.readline())


def R(l):
    return l[::-1]


def D(l):
    if len(l) == 0:
        return False
    else:
        return l[1::]


for _ in range(N):
    func = sys.stdin.readline()
    count_D = func.count('D')
    list_len = int(sys.stdin.readline())
    if list_len == 0:
        list1 = sys.stdin.readline()
        list1 = list()
    else:
        list1 = sys.stdin.readline()
        list1 = list1[1:-2]
        list1 = list(map(int, list1.split(',', list_len-1)))

    if list_len < count_D:
        print('error')
    else:
        for f in func:

            if f == 'R':
                list1 = R(list1)
            elif f == 'D':
                list1 = D(list1)
        print(list1)


