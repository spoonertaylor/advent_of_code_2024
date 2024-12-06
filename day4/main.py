# Advent of Code, Day 4

def read_input():
    with open('input_file.txt') as f:
        return f.read().splitlines()

# Count the number of times a word (or its reverse) shows up in our matrix
def count_horizontal(l, word):
    reverse_word = word[::-1]
    main_word_count = 0
    reverse_word_count = 0
    # For each row in the list
    # Count the times the word and reverse shows up
    for r in range(len(l)):
        if word in l[r]:
            main_word_count += l[r].count(word)
        if reverse_word in l[r]:
            reverse_word_count += l[r].count(reverse_word)
    return main_word_count + reverse_word_count

def transpose_input(l):
    return list(map(list, zip(*l)))

def count_vertical(l, word):
    reverse_word = word[::-1]
    # Transpose input to make vertical letters in the same row (count_horizontal)
    l_t = transpose_input(l)
    l_t_join = ["".join(i) for i in l_t]
    # Count occurances
    return count_horizontal(l_t_join, word)

# To count the diagonals: Loop through every element in the matrix.
# Create a key for each diagonal option and store the value,
# building each diagonal as a horizontal row as we go
def count_diagonals(l, word):
    reverse_word = word[::-1]
    rows = len(l)
    columns = len(l[0])

    diagonal = {}
    anti_diagonal = {}
    for r in range(rows):
        for c in range(columns):
            key_main = r - c
            if key_main not in diagonal:
                diagonal[key_main] = []
            diagonal[key_main].append(l[r][c])

            key_anti = r + c
            if key_anti not in anti_diagonal:
                anti_diagonal[key_anti] = []
            anti_diagonal[key_anti].append(l[r][c])

    diagonal_l = ["".join(i) for i in diagonal.values()]
    anti_diagonal_l = ["".join(i) for i in anti_diagonal.values()]

    return count_horizontal(diagonal_l, word) + count_horizontal(anti_diagonal_l, word)

def count_occurances(l, word):
    return count_horizontal(l, word) + count_vertical(l, word) + count_diagonals(l, word)

def check_xmas(l, r, c, word):
    reverse_word = word[::-1]
    rows = len(l)
    columns = len(l[0])

    # Check if in bounds
    # Diagonal goes up 1 to the left or right
    # and down 1 to the left or right
    if (r - 1 < 0) or r + 1 >= rows or c - 1 < 0 or c + 1 >= columns:
        return False

    # Create the diagonal X
    main_diag = ''.join([l[r-1][c-1], l[r][c], l[r+1][c+1]])
    anti_diag = ''.join([l[r-1][c+1], l[r][c], l[r+1][c-1]])
    # Check that the word or reverse of word is in both
    if ((word in main_diag or reverse_word in main_diag) and
        (word in anti_diag or reverse_word in anti_diag)):
        return True

    return False

def count_xmas(l, word):
    rows = len(l)
    columns = len(l[0])

    x_count = 0
    # Loop through all options in the list
    for r in range(1, rows-1):
        for c in  range(1, columns-1):
            if check_xmas(l, r, c, word):
                x_count += 1

    return x_count

if __name__ == "__main__":
    letters = read_input()
    print(f"Number of occurances: {count_occurances(letters, 'XMAS')}")
    print(f"Number of x's: {count_xmas(letters, 'MAS')}")
