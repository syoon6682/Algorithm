'''
재귀적 풀이..!
'''

import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):

    def grouping(s, e):
        if s == e:
            return s
        else:
            left = grouping(s, (s+e)//2)
            right = grouping((s+e)//2+1, e)
            return game(left, right)

    def game(l, r):
        if student[l] == 1:
            if student[r] == 2:
                return r
            else:
                return l

        if student[l] == 2:
            if student[r] == 3:
                return r
            else:
                return l

        if student[l] == 3:
            if student[r] == 1:
                return r
            else:
                return l

    N = int(input())
    student = list(map(int, input().split()))
    student = [0] + student
    result = grouping(1,N)

    print(f'#{tc} {result}')

