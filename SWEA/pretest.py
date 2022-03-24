T = int(input())
for test_case in range(1, T + 1):
    X, Y = map(float, input().split())
    h = ((4 * (X + Y)) - (16 * X * X - 16 * X * Y + 16 * Y * Y) ** (0.5)) / 24
    result = h * (X - 2*h) * (Y - 2*h)
    print(f"#{test_case} {result: .6f}")
