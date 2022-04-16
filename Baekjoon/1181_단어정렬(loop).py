N = int(input())

word = list()
test = list()
for i in range(N):
    test.append(input())

print(test)

for t in test:
    if not word:
        word.append(t)
        continue
    else:
        for w in word:
            if len(t) < len(w):
                word.insert(word.index(w), t)
                print(word)
                break
            elif len(t) > len(w):
                continue
            else:
                if w == t:
                    break
                for j in range(len(w)):
                    if ord(w[j]) > ord(t[j]):
                        word.insert(word.index(w), t)
                    elif ord(w[j]) > ord(t[j]):
                        break


        else:
            word.append(t)

for w in word:
    print(w)
