def powerset(idx, N):

    if idx == N:  # 종료 조건
        print(bit)
        return

    bit[idx] = 0
    powerset(idx + 1, N)

    bit[idx] = 1
    powerset(idx + 1, N)


a = [0, 7, 2, 3]
N = len(a)
bit = [0] * N

powerset(idx=0, N=N)