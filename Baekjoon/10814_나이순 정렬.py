N = int(input())

person = list()
for i in range(N):
    person.append(list(map(str, input().split())))

age = [0] * 201
for p in person:
    age[int(p[0])] += 1

for i in range(len(age)):
    cnt = 0
    while age[i] != 0:
        if int(person[cnt][0]) == i:
            print(person[cnt][0], person[cnt][1])
            age[i] -= 1
        cnt += 1
