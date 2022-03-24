import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    word_list = []
    len_max_list = 0
    for _ in range(5):
        a = list(input())
        word_list.append(a)
        if len(a) > len_max_list:
            len_max_list = len(a)

    col_word = ''
    for i in range(len_max_list):
        for j in range(5):
            try:
                col_word += word_list[j][i]
            except IndexError:
                pass

    print(f'#{tc} {col_word}')

