S = input()
num_list = [0]*10
for s in S:
    num_list[int(s)] += 1
new_num = ''
for i in range(9, -1 ,-1):
    new_num += str(i)*num_list[i]

print(int(new_num))