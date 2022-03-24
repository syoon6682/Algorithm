num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in num_list:
    for j in range(3):
        print(i[j], end=' ')

print('')
"----------------------------"
"델타를 활용한 원하는 방향 검색! 이거는 진짜 신박하긴 한듯"

for i in range(len(num_list)):
    for j in range(len(num_list[i])):
        print(num_list[i][j], end=' ')

dx = [(1,0), (-1,0), (0,1), (0,-1)]

for i, j in dx:
    print(num_list[1+i][1+j], end='')