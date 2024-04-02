import random

class MagicSquare:
    def __init__(self):
        self.grid = [[0] * 3 for _ in range(3)]

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def generate_puzzle(self):
        self.grid = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        for _ in range(100):
            row, col = self.find_number(9)
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random_move = random.choice(moves)
            new_row, new_col = row + random_move[0], col + random_move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                self.grid[row][col], self.grid[new_row][new_col] = self.grid[new_row][new_col], self.grid[row][col]

    def find_number(self, num):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == num:
                    return i, j
        return -1, -1

    def is_magic_square(self):
        rows = [sum(row) for row in self.grid]
        cols = [sum(col) for col in zip(*self.grid)]
        diagonals = [sum(self.grid[i][i] for i in range(3)), sum(self.grid[i][2 - i] for i in range(3))]
        return all(row == cols[0] for row in rows) and all(row == diagonals[0] for row in rows)

    def solve_puzzle(self):
        if self.is_magic_square():
            return

        best_score = float('inf')
        best_grid = None

        for _ in range(1000):
            new_grid = [row[:] for row in self.grid]  
            row1, col1 = random.randint(0, 2), random.randint(0, 2)
            row2, col2 = random.randint(0, 2), random.randint(0, 2)

            new_grid[row1][col1], new_grid[row2][col2] = new_grid[row2][col2], new_grid[row1][col1]

            score = sum(abs(new_grid[i][j] - ((i * 3) + j + 1)) for i in range(3) for j in range(3))

            if score < best_score:
                best_score = score
                best_grid = new_grid

        self.grid = best_grid

def main():
    print("\nMagic Square Puzzle:")
    magic_square_solver = MagicSquare()
    magic_square_solver.generate_puzzle()
    magic_square_solver.print_grid()

    print("\nSolving Magic Square:")
    magic_square_solver.solve_puzzle()
    magic_square_solver.print_grid()

if __name__ == "__main__":
    main()
