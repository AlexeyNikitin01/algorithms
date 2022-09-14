def search_substring(word_a: str, word_b: str):
    cell = [[0 for _ in range(len(word_b))] for _ in range(len(word_a))]
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                cell[i][j] = cell[i-1][j-1]+1
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    return cell


if __name__ == '__main__':
    word_a = 'blue'
    word_b = 'clues'
    cell = search_substring(word_a, word_b)
    for i in range(len(cell)):
        print(cell[i])
    print(f'max substring == {cell[-1][-1]}')
