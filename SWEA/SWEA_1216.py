import sys

sys.stdin = open('input.txt')


for tc in range(1, 11):
    T = int(input())
    total_list = []
    for _ in range(100):
        total_list.append(input())

    # 가로방향
    max_row = 0
    for length in range(100, 0, -1): # 100부터 찾아서
        for word in total_list:
            for k in range(100 - length + 1):
                test_word = word[k:k + length] # 원하는 길이, 위치로 슬라이싱
                for i in range(length): # 회문 테스트
                    if test_word[i] != test_word[-1-i]:
                        break
                # 이 아래로는 회문을 찾았으면 루프를 벗어나기 위한 코드
                else:
                    max_row = len(test_word)
                    break

            if max_row != 0:
                break

        if max_row != 0:
            break


    # 세로방향
    max_col = 0
    for length in range(100, 0, -1):
        for idx in range(100):
            temp_list = []
            for lst in total_list:
                temp_list.append(lst[idx])
            for k in range(100 - length + 1):
                test_word = temp_list[k:k + length]
                for i in range(length):
                    if test_word[i] != test_word[-1 - i]:
                        break
                else:
                    max_col = len(test_word)
                    break

            if max_col != 0:
                break

        if max_col != 0:
            break

    if max_row > max_col:
        print(f'#{tc} {max_row}')
    else:
        print(f'#{tc} {max_col}')
