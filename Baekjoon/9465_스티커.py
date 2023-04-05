T = int(input())

for _ in range(T):
    n = int(input())
    upper = list(map(int, input().split()))
    under = list(map(int, input().split()))

    A = list()
    B = list()
    for i in range(n):
        if i == 0:
            A.append(upper[i])
            B.append(under[i])
        else:
            A.append(max(B[i-1] + upper[i], A[i-1]))
            B.append(max(A[i-1] + under[i], B[i-1]))

    print(max(A[-1], B[-1]))
