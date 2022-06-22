def rev(n):
    n = str(n)
    return int(n[::-1])


a, b = map(int, input().split())

print(rev(rev(a)+rev(b)))