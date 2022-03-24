import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    price_list = list(map(int, input().split()))
    total_profit = 0

    for i in range(len(price_list)):
        max_price = 0
        product_profit = 0

        for j in range(i, len(price_list)):
            if price_list[i] < price_list[j] and price_list[j] > max_price:
                max_price = price_list[j]
                product_profit = max_price - price_list[i]

        total_profit = total_profit + product_profit

    print(f'#{tc} {total_profit}')

