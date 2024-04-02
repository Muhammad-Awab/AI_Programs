import random

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def generate_puzzle(self):
        pass

    def solve_puzzle(self):
        pass

class Sudoku(Puzzle):
    def __init__(self):
        super().__init__(9)

    def generate_puzzle(self):
        self.solve_puzzle()
        to_remove = random.randint(40, 50)
        for _ in range(to_remove):
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0

    def is_valid_move(self, row, col, num):
        if num in self.grid[row]:
            return False
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def solve_puzzle(self):
        def backtrack(row, col):
            if row == 9:
                return True
            next_row = row + 1 if col == 8 else row
            next_col = (col + 1) % 9
            if self.grid[row][col] != 0:
                return backtrack(next_row, next_col)
            for num in range(1, 10):
                if self.is_valid_move(row, col, num):
                    self.grid[row][col] = num
                    if backtrack(next_row, next_col):
                        return True
                    self.grid[row][col] = 0
            return False

        return backtrack(0, 0)

def main():
    print("Sudoku Puzzle:")
    sudoku_solver = Sudoku()
    sudoku_solver.generate_puzzle()
    sudoku_solver.print_grid()
    print("\nSolving Sudoku:")
    sudoku_solver.solve_puzzle()
    sudoku_solver.print_grid()
    
if __name__ == "__main__":
    main()
