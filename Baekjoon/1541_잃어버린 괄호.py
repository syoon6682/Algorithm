S = input()

num = ''
num_list = list()
oper_list = list()

for s in S:
    if s != '-' and s != '+':
        num += s
    else:
        num_list.append(int(num))
        num = ''
        oper_list.append(s)
num_list.append(int(num))

answer = 0

if '-' not in oper_list:
    answer = sum(num_list)
else:
    std = oper_list.index('-')
    for i in range(0, std+1):
        answer += num_list[i]
    for j in range(std+1, len(num_list)):
        answer -= num_list[j]

print(answer)