T = int(input())
triangle = [1, 1, 1, 2, 2]

for i in range(5, 101):
    triangle.append(triangle[i-1] + triangle[i-5])

for j in range(T):
    print(triangle[int(input())-1])
