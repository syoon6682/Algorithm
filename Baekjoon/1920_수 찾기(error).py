N = int(input())
num = list(map(int, input().split()))

num.sort()

M = int(input())
test = list(map(int, input().split()))

for t in test:
    first = 0
    last = len(num)-1
    while first < last:
        mid = (first + last) // 2
        if num[first] == t or num[last] == t or num[mid] == t:
            print(1)
            break
        elif t < num[first] or t > num[last]:
            print(0)
            break
        elif t > num[mid]:
            first = mid + 1
        elif t < num[mid]:
            last = mid - 1
    else:
        print(0)
