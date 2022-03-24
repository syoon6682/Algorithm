import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    search = input()
    test_word = input()
    count_dic = {} # 데이터 입력 받기

    for i in search: # search의 항목이
        if not (i in count_dic): # key에 없으면
            cnt = 0
            for j in test_word: # test_word와 비교하며 카운트
                if i == j:
                    cnt += 1
            count_dic[i] = cnt # 딕셔너리에 저장

    # 딕셔너리 안에서 가장 큰 값 찾기
    count_max = 0
    for val in count_dic.values():
        if val > count_max:
            count_max = val

    print(f'#{tc} {count_max}')

