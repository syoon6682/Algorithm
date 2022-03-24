import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    total_len, target_len = map(int, input().split())
    total_list = []
    for i in range(total_len):
        temp_word = input()
        temp_list = [i for i in temp_word]
        total_list.append(temp_list)

    for i in range(total_len):
        for j in range(total_len - target_len + 1):
            start = j
            end = start + target_len - 1
            while start < end - 1:
                if total_list[i][start] == total_list[i][end]:
                    start += 1
                    end -= 1
                else:
                    break
            else:
                print(f'#{tc} ', end='')
                for k in total_list[i][j:j+target_len]:
                    print(k, end='')
                print('')

    # 세로 계산
    for i in range(total_len):
        for j in range(total_len - target_len + 1):
            start = j
            end = start + target_len - 1
            while start < end - 1:
                if total_list[start][i] == total_list[end][i]:
                    start += 1
                    end -= 1
                else:
                    break
            else:
                print(f'#{tc} ', end='')
                for k in total_list[j:j+target_len][i]:
                    print(k, end='')
                print('')
