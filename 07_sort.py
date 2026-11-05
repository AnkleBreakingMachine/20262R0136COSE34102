
def bubble_sort(arr):
    result = arr.copy()
    n = len(result)

    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = (
                    result[j + 1], result[j]
                )
    return result

print(bubble_sort([5, 2, 9, 1, 7]))