def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort(arr, low, high):
    if low == high:
        return 1

    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


x = [12, 43, 2, 9, 32, 87, 43, 21, 27, 1, 39]
quick_sort(x, 0, len(x)-1)

for z in range(len(x)):
    print("{}, ".format(x[z]), end='')
