powerset = [x for x in range(1, 11)]
bit = [0]*10


def cal(idx, N, tot): # index, 제한사항, 전체 합을 parameter로 넣기
    if idx == N: # 종료 조건에 도달했는데
        if tot == 10: # 총합이 10이면
            for i in range(10): # print 해주고
                if bit[i] == 1:
                    print(powerset[i], end=' ')
            print() # 줄바꿔주기

        return

    bit[idx] = 1
    tot += powerset[idx]
    if tot <= 10: # 아직 총합이 10 이하일 때 부분 집합에 다른 숫자 추가
        cal(idx + 1, N, tot)
    tot -= powerset[idx]

    bit[idx] = 0
    cal(idx + 1, N, tot)



cal(0, 10, 0)
