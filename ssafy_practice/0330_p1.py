import sys

sys.stdin = open('input.txt')


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while right > left and pivot >= arr[left]:
            left += 1
        while right > left and pivot <= arr[right]:
            right -= 1

        if left == right:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:  # 교차하지 않는다면
        pivot = partition(arr, start, end)  # pivot 설정하고
        quick_sort(arr, start, pivot-1)  # 왼쪽 정렬
        quick_sort(arr, pivot+1, end)  # 오른쪽 정렬
    return arr


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    A = quick_sort(numbers, 0, len(numbers) - 1)  # 정렬 할 배열, 시작 ~ 끝 idx
    print(f'#{tc} {A[N // 2]}')