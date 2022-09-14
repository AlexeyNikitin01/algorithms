def search_max_price(cell, element, weight_backpack, i) -> int:
    weight_product = element[0]
    price_product = element[1]
    max_price = 0

    if i == 0:
        if weight_backpack >= weight_product:
            max_price = price_product
            return max_price
        else:
            return 0

    if i > 0:
        if weight_backpack >= weight_product:
            if weight_backpack - weight_product > 0:
                max_price = max(cell[i-1][weight_backpack-1], price_product + cell[i-1][weight_backpack-1-weight_product])
            elif weight_backpack - weight_product == 0:
                max_price = max(cell[i-1][weight_backpack-1], price_product)
        else:
            max_price = cell[i - 1][weight_backpack - 1]

    return max_price


def max_elem_in_backpack(elements: dict, weight_backpack: int) -> int:
    cell = [[] for _ in range(len(elements))]

    for i, element in enumerate(elements.values()):
        for j in range(1, weight_backpack+1):
            max_price = search_max_price(cell, element, j, i)
            cell[i].append(max_price)
    print(cell)
    return cell[-1][-1]


if __name__ == '__main__':
    elements = {
        'water': (3, 10),
        'book': (1, 3),
        'food': (2, 9),
        'jacket': (2, 5),
        'camera': (1, 6),
    }
    weight_backpack = 6
    result = max_elem_in_backpack(elements, weight_backpack)
    print(result)

# ответ на 9.1 вода еда камера