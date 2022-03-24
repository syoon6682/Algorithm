N = int(input())

dice_inform = []
for _ in range(N):
    temp_dice = list(map(int, input().split()))
    dice_inform.append(temp_dice)


max_sum = 0

for i in range(1, 7):
    downside_num = i
    total_sum = 0

    for j in dice_inform:
        downside_index = j.index(downside_num)
        if downside_index == 0:
            upside_index = 5
        elif downside_index == 1:
            upside_index = 3
        elif downside_index == 2:
            upside_index = 4
        elif downside_index == 3:
            upside_index = 1
        elif downside_index == 4:
            upside_index = 2
        elif downside_index == 5:
            upside_index = 0

        if j[downside_index] == 6 or j[upside_index] == 6:
            if j[downside_index] == 5 or j[upside_index] == 5:
                total_sum += 4
            else:
                total_sum += 5
        else:
            total_sum += 6

        downside_num = j[upside_index]

    if total_sum > max_sum:
        max_sum = total_sum

print(max_sum)
