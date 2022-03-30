# 데이터 다 받고 부모, 자식 list 생성, visited 생성
V, N = map(int, input().split())
arr = list(map(int, input().split()))
par = [0]*(V+1)
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)


# 부모, 자식을 정리해주기
for i in range(N):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

# 자식 번호를 기준으로 부모 저장
for i in range(N):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p

# 시작점 찾기 -> 부모가 없으면 시작점
for i in range(1,N+1):
    if par[i] == 0:
        anc = i


def preorder(s):
    if len(visited) != N:
        visited.append(s)

        if ch1[s] != 0:
            preorder(ch1[s])
        if ch2[s] != 0:
            preorder(ch2[s])

    return visited


def inorder(s):
    if len(visited) != N:
        if ch1[s] != 0:
            preorder(ch1[s])
        visited.append(s)
        if ch2[s] != 0:
            preorder(ch2[s])

    return visited


def postorder(s):
    if len(visited) != N:
        if ch1[s] != 0:
            preorder(ch1[s])

        if ch2[s] != 0:
            preorder(ch2[s])

        visited.append(s)

    return visited


visited = list()
result = preorder(anc)
print(result)

visited.clear()
result = inorder(anc)
print(result)

visited.clear()
result = postorder(anc)
print(result)
