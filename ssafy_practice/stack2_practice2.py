
def powerset(idx, N):

    if idx == N: # 0과 1로 bit를 다 채웠을 때 출력하기 위한 작업
        temp_sum = 0
        for i in range(len(bit)): # 부분집합의 합을 구함
            if bit[i] == 1:
                temp_sum += a[i]
        if temp_sum == 10: # 근데 그게 10이면 부분집합을 출력
            temp_list = []
            for i in range(len(bit)):
                if bit[i] == 1:
                    temp_list.append(a[i])
            print(temp_list)
        return

    else:
        bit[idx] = 1 # 먼저 [1,1,1,1,1,1,1,1,1,1]을 만들기 위한 작업
        powerset(idx+1, N)
        bit[idx] = 0 # 다음 0을 순서대로 순회하기 위한 작업
        powerset(idx + 1, N)


a = [i for i in range(1,11)]
N = len(a)
bit = [0] * N

powerset(idx=0, N=N)
