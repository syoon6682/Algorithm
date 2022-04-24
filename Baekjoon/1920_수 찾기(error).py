N = int(input())
num = list(map(int, input().split()))
arr_plus = [0]*2147483648
arr_minus = [0]*2147483648
for n in num:
    if n >= 0:
        arr_plus[n] += 1
    else:
        arr_minus[-n] += 1

M = int(input())
test = list(map(int, input().split()))
for t in test:
    if t >= 0:
        if arr_plus[t] > 0:
            print(1)
        else:
            print(0)
    else:
        if arr_minus[-t] > 0:
            print(1)
        else:
            print(0)

