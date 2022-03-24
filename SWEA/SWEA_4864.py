import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    small_list = input()
    large_list = input() # 데이터 입력 받기

    for i in range(len(large_list) - len(small_list) + 1):
        if large_list[i] == small_list[0]: # small 첫 글자가 일치하면
            if large_list[i:i+len(small_list)] == small_list: # 뒤도 다 같은지 판별 후
                print(f'#{tc} 1') # 맞으면 1 출력
                break
    else:
        print(f'#{tc} 0') # 없으면 0 출력

