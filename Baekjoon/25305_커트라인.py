N, M = map(int, input().split())

appliance = list(map(int, input().split()))

appliance.sort(reverse=True)

print(appliance[M-1])