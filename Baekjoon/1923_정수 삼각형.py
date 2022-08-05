N = int(input())

note = list()
for i in range(N):
    if i == 0:
        note.append(int(input()))
    else:
        temp = list(map(int, input().split()))
        # print(temp)
        # print(note)
        new_note = list()
        for j in range(len(temp)):
            if j == 0:
                new_note.append(note[j] + temp[j])
            elif j == len(temp)-1:
                new_note.append(note[j-1] + temp[j])
                # print(new_note)
            else:
                new_note.append(max(note[j-1] + temp[j], note[j] + temp[j]))
        note = new_note[:]

print(max(note))
