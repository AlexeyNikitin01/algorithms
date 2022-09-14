
def merge_sort(queue: list) -> list:

    if len(queue) < 2:
        return queue[:]

    left = queue[:len(queue) // 2]
    right = queue[len(queue) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    i = 0
    j = 0
    sorted_queue = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_queue.append(left[i])
            i += 1
        else:
            sorted_queue.append(right[j])
            j += 1

    sorted_queue += left[i:]
    sorted_queue += right[j:]

    return sorted_queue


if __name__ == '__main__':
    queue = [1, 5, 2, 3, 9]
    print(merge_sort(queue))
