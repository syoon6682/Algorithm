N = int(input())
num = list()
for i in range(1, N+1):
    num.append(i)

pointer = 0

while len(num) > pointer:
    if pointer % 2 == 0:
        pointer += 1
    else:
        num.append(num[pointer])
        pointer += 1

print(num[pointer-1])
