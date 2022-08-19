N = int(input())

test = list()
for _ in range(N):
    test.append(input())


length = len(test[0])
answer = ''

for i in range(length):
    temp = test[0][i]
    for s in test:
        if s[i] != temp:
            answer += '?'
            break
    else:
        answer += temp

print(answer)