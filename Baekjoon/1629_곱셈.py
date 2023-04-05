A, B, C = map(int, input().split())

remain = list()
x = 1
for _ in range(B):
    x *= A
    x = x % C
    if x not in remain:
        remain.append(x)
    else:
        break

# print(remain)

# 모든 나머지가 다른 경우
if len(remain) == B:
    print(remain[-1])
else:
    ind = remain.index(x)
    loop_list = remain[ind:]
    # print(ind)
    # print("loop: ", loop_list)
    B -= ind
    B %= len(loop_list)
    print(loop_list[B])
# print(remain)
# print(x)