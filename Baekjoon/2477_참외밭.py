K = int(input())

length = list()
for _ in range(6):
    length.append(list(map(int, input().split())))

direc = list()
for l in length:
    direc.append(l[0])

test = list()
tot_list = list()
for i in range(1 ,5):
    if direc.count(i) == 2:
        test.append(i)
    else:
        tot_list.append(i)

tot = length[direc.index(tot_list[0])][1] * length[direc.index(tot_list[1])][1]
a, b = test[0], test[1]


for i in range(-6, 3):
    if ((direc[i] == a and direc[i+1] == b and direc[i+2] == a and direc[i+3] == b) or
    (direc[i] == b and direc[i+1] == a and direc[i+2] == b and direc[i+3] == a)):
        minus = length[i+1][1] * length[i+2][1]
        break

print((tot-minus)*K)
