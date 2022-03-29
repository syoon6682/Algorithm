import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    player_1 = list()
    player_2 = list()
    rlt = 0 # 아무 결과가 안나오면 무승부이므로 0으로 시작

    def babygin(l):
        index_list = [0]*10

        # index list 변환
        for i in l:
            index_list[i] += 1

        # triplet 판단
        for i in range(10):
            if index_list[i] >= 3:
                return 'win'
        # run 판단
        for j in range(8):
            if index_list[j] >= 1 and index_list[j+1] >= 1 and index_list[j+2] >= 1:
                return 'win'

        return 'yet'

    # win return 하면 반복문 바로 끝내고 승자를 rlt에 저장
    for c in range(12):
        if c%2 == 0:
            player_1.append(card[c])
            result = babygin(player_1)
            if result == 'win':
                rlt = 1
                break
        else:
            player_2.append(card[c])
            result = babygin(player_2)
            if result == 'win':
                rlt = 2
                break

    print(f'#{tc} {rlt}')

