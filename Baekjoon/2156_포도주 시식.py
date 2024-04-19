n = int(input())

grapes = list()

for i in range(n):
    grapes.append(int(input()))

if n == 1:
    print(grapes[n-1])
elif n == 2:
    print(grapes[0] + grapes[1])
elif n == 3:
    print(max(grapes[0]+ grapes[2], grapes[1] + grapes[2], grapes[0] + grapes[1]))
else:
    dp = list(0 for _ in range(n))

    dp[0] = grapes[0]
    dp[1] = grapes[0] + grapes[1]
    dp[2] = max(grapes[0]+ grapes[2], grapes[1] + grapes[2], grapes[0] + grapes[1])

    for i in range(3,n):
        a = dp[i-3] + grapes[i-1] + grapes[i]
        b = dp[i-2] + grapes[i]
        
        drink_max = max(a,b)
        undrink_max = dp[i-1]
        
        dp[i] = max(drink_max, undrink_max)
        
    print(dp[-1])
