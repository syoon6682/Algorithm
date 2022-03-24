import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


def routing(s, e):
    if s == e:
        return 1
    else:
        for i in node_list:
            if i[0] == s:
                new_s = i[1]
                r = routing(new_s, e)
                if r == 1:
                    return 1

        else:
            return 0


for tc in range(1, T + 1):

    V, E = map(int, input().split())
    node_list = list()
    for _ in range(E):
        temp_list = list(map(int, input().split()))
        node_list.append(temp_list)
    start, end = map(int, input().split())
    result = routing(start, end)

    print(f'#{tc} {result}')

