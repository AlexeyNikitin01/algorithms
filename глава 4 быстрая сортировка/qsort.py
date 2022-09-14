#  QuickSort - быстрая сортировка

from random import choice


def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    pivot = choice(arr)

    left_part = [i for i in arr if i < pivot]
    right_part = [j for j in arr if j > pivot]
    pivots = [y for y in arr if y == pivot]
    return quick_sort(left_part) + pivots + quick_sort(right_part)


if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 5, 6, 6, 6, 1, 4, 5]
    sort_arr = quick_sort(arr)
    print(sort_arr)
