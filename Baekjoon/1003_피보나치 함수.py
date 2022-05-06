N = int(input())


class Fibo:
    def __init__(self, zero, one):
        self.zero = zero
        self.one = one


fibo_list = list()
for i in range(41):
    if i == 0:
        fibo_list.append(Fibo(1, 0))
    elif i == 1:
        fibo_list.append(Fibo(0, 1))
    else:
        fibo_list.append(Fibo(fibo_list[i-1].zero + fibo_list[i-2].zero, fibo_list[i-1].one + fibo_list[i-2].one))


for i in range(N):
    n = int(input())
    print(fibo_list[n].zero, fibo_list[n].one)
