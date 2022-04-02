M, N = map(int, input().split())
num_list = [1]*(N+1)
num_list[0], num_list[1] = 0, 0

i = 2
while i ** 2 <= N:
    if num_list[i] == 1:
        temp = 2
        while temp*i <= N:
            num_list[temp * i] = 0
            temp += 1
        i += 1
    while num_list[i] == 0 and i**2 <= N:
        i += 1


for j in range(M, N+1):
    if num_list[j] == 1:
        print(j)

