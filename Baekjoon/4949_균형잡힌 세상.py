T = list()

while True:
    temp = input()
    if temp == '.':
        break
    else:
        T.append(temp)

for t in T:
    stack = list()
    for s in t:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack:
                print('no')
                break
            else:
                p = stack.pop()
                if p != '(':
                    print('no')
                    break
        elif s == ']':
            if not stack:
                print('no')
                break
            else:
                p = stack.pop()
                if p != '[':
                    print('no')
                    break
    else:
        if not stack:
            print('yes')
        else:
            print('no')
