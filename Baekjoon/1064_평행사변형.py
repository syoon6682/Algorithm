from math import sqrt

x1, y1, x2, y2, x3, y3 = map(float, input().split())

def distance(a, b, c, d):
    return sqrt((a-b)**2 + (c-d)**2)


if (x3-x1) / (x2-x1) == (y3-y1) / (y2-y1):
    print(-1)
else:
    maximum = max(distance(x1, x2, y1, y2) + distance(x1, x3, y1, y3), distance(x1, x2, y1, y2) + distance(x2, x3, y2, y3), distance(x1, x3, y1, y3) + distance(x2, x3, y2, y3))
    minimum = max(distance(x1, x2, y1, y2) + distance(x1, x3, y1, y3), distance(x1, x2, y1, y2) + distance(x2, x3, y2, y3), distance(x1, x3, y1, y3) + distance(x2, x3, y2, y3))
    print((maximum-minimum)*2)