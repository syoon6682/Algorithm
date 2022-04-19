x_point = list()
y_point = list()
for i in range(3):
    temp = list(map(int,input().split()))
    x_point.append(temp[0])
    y_point.append(temp[1])

if x_point.count(x_point[0]) == 1:
    rest_x = x_point[0]
else:
    if x_point[0] == x_point[2]:
        rest_x = x_point[1]
    else:
        rest_x = x_point[2]

if y_point.count(y_point[0]) == 1:
    rest_y = y_point[0]
else:
    if y_point[0] == y_point[2]:
        rest_y = y_point[1]
    else:
        rest_y = y_point[2]
print(rest_x, rest_y)

