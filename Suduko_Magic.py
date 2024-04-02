import numpy as np
import random

def generate_sudoku():
    # Initialize empty 9x9 grid
    grid = np.zeros((9, 9), dtype=int)
    # Fill the diagonal boxes
    for i in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for j in range(3):
            for k in range(3):
                grid[i+j][i+k] = nums.pop()
    # Solve the puzzle
    solve_sudoku(grid)
    # Remove some numbers to create the puzzle
    puzzle = np.copy(grid)
    num_to_remove = random.randint(40, 60)  # Adjust the range for desired difficulty
    for _ in range(num_to_remove):
        i, j = random.randint(0, 8), random.randint(0, 8)
        while puzzle[i][j] == 0:
            i, j = random.randint(0, 8), random.randint(0, 8)
        puzzle[i][j] = 0
    return puzzle

def is_valid_move(grid, row, col, num):
    # Check if the number is not already in the row
    if num in grid[row]:
        return False
    # Check if the number is not already in the column
    if num in grid[:, col]:
        return False
    # Check if the number is not already in the 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    if num in grid[box_row:box_row+3, box_col:box_col+3]:
        return False
    return True

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # Puzzle solved
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Example usage:
if __name__ == "__main__":
    puzzle = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    print_sudoku(puzzle)
    print("\nSolved Sudoku Puzzle:")
    solve_sudoku(puzzle)
    print_sudoku(puzzle)


# In[5]:


import numpy as np
import random

def generate_magic_square():
    # Initialize magic square with numbers 1 to 9
    magic_square = np.arange(1, 10).reshape(3, 3)
    # Set the movable number to 9
    magic_square[2, 2] = 9
    # Shuffle the numbers to create a random puzzle
    np.random.shuffle(magic_square.flat[:-1])  # Exclude the last element (movable number)
    return magic_square

def is_valid_move(magic_square, row, col, num):
    # Check if the number is not already in the row, column, or 3x3 box
    return (num not in magic_square[row]) and \
           (num not in magic_square[:, col]) and \
           (num not in magic_square[row//3*3:row//3*3+3, col//3*3:col//3*3+3])

def find_next_empty_cell(magic_square):
    min_options = 10  # Initialize with a value greater than possible options
    next_cell = None
    for row in range(3):
        for col in range(3):
            if magic_square[row, col] == 9:
                options = count_valid_options(magic_square, row, col)
                if options < min_options:
                    min_options = options
                    next_cell = (row, col)
    return next_cell

def count_valid_options(magic_square, row, col):
    options = 0
    for num in range(1, 10):
        if is_valid_move(magic_square, row, col, num):
            options += 1
    return options

def solve_magic_square(magic_square):
    empty_cell = find_next_empty_cell(magic_square)
    if empty_cell is None:
        return True  # Puzzle solved
    else:
        row, col = empty_cell
        for num in range(1, 10):
            if is_valid_move(magic_square, row, col, num):
                magic_square[row, col] = num
                if solve_magic_square(magic_square):
                    return True
                magic_square[row, col] = 9  # Reset the cell
    return False

def print_magic_square(magic_square):
    for row in magic_square:
        print(" ".join(map(str, row)))

# Example usage:
if __name__ == "__main__":
    magic_square = generate_magic_square()
    print("Generated Magic Square Puzzle:")
    print_magic_square(magic_square)
    print("\nSolved Magic Square Puzzle:")
    solve_magic_square(magic_square)
    print_magic_square(magic_square)


# In[ ]:





# In[ ]:

