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
        for w in range(len(word)):
            if len(t) < len(word[w]):
                word.insert(w, t)
                print(word)
                break
            elif len(t) > len(word[w]):
                continue
            else:
                if word[w] == t:
                    break
                cnt = 0
                while True:
                    if ord(word[w][cnt]) > ord(t[cnt]):
                        

                break



        else:
            word.append(t)

for w in word:
    print(w)
