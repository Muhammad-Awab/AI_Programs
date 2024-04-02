#include <iostream>
#include <cstdlib>
#include <ctime>

class Puzzle {
protected:
    int size;
    int** grid;

public:
    Puzzle(int size) : size(size) {
        grid = new int*[size];
        for (int i = 0; i < size; ++i) {
            grid[i] = new int[size];
            for (int j = 0; j < size; ++j) {
                grid[i][j] = 0;
            }
        }
    }

    void printGrid() {
        for (int i = 0; i < size; ++i) {
            for (int j = 0; j < size; ++j) {
                cout << grid[i][j] << " ";
            }
            cout << endl;
        }
    }

    virtual void generatePuzzle() = 0;
    virtual bool solvePuzzle() = 0;

    virtual ~Puzzle() {
        for (int i = 0; i < size; ++i) {
            delete[] grid[i];
        }
        delete[] grid;
    }
};

class Sudoku : public Puzzle {
public:
    Sudoku() : Puzzle(9) {}

    void generatePuzzle() override {
        solvePuzzle();
        int toRemove = rand() % 11 + 40;
        for (int i = 0; i < toRemove; ++i) {
            int row = rand() % 9;
            int col = rand() % 9;
            grid[row][col] = 0;
        }
    }

    bool isSafeMove(int row, int col, int num) {
        for (int i = 0; i < size; ++i) {
            if (grid[row][i] == num || grid[i][col] == num) {
                return false;
            }
        }

        int startRow = 3 * (row / 3);
        int startCol = 3 * (col / 3);
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (grid[startRow + i][startCol + j] == num) {
                    return false;
                }
            }
        }
        return true;
    }

    bool solvePuzzle() override {
        return solve(0, 0);
    }

private:
    bool solve(int row, int col) {
        if (row == size) {
            return true;
        }
        int nextRow = (col == size - 1) ? row + 1 : row;
        int nextCol = (col + 1) % size;
        if (grid[row][col] != 0) {
            return solve(nextRow, nextCol);
        }
        for (int num = 1; num <= size; ++num) {
            if (isSafeMove(row, col, num)) {
                grid[row][col] = num;
                if (solve(nextRow, nextCol)) {
                    return true;
                }
                grid[row][col] = 0;
            }
        }
        return false;
    }
};

int main() {
    srand(time(nullptr));

    cout << "Sudoku Puzzle:" << endl;
    Sudoku sudokuSolver;
    sudokuSolver.generatePuzzle();
    sudokuSolver.printGrid();

    cout << "\nSolving Sudoku:" << endl;
    sudokuSolver.solvePuzzle();
    sudokuSolver.printGrid();

    return 0;
}
