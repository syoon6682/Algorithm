K, N = map(int, input().split())

lan = list()
start = 1
end = 0
for _ in range(K):
    temp = int(input())
    lan.append(temp)
    end = max(end, temp)

answer = 1


def binary(s, e):
    global answer
    mid = (s + e) // 2

    if s > e:
        return
    local_sum = 0
    for l in lan:
        local_sum += l//mid

    if local_sum >= N:
        answer = mid
        binary(mid + 1, e)
    else:
        binary(s, mid-1)




binary(start, end)
print(answer)
