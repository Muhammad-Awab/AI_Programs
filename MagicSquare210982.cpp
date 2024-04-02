#include <iostream>
#include <cstdlib>
#include <ctime>
#include <unordered_set>
using namespace std;

const int SIZE = 3;

void initializeSquare(int square[SIZE][SIZE]) {
    int num = 1;
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            square[i][j] = num++;
        }
    }
}

void printSquare(int square[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            cout << square[i][j] << " ";
        }
        cout << endl;
    }
}

bool isValidMove(int x, int y) {
    return x >= 0 && x < SIZE && y >= 0 && y < SIZE;
}

void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

bool isMagicSquare(int square[SIZE][SIZE]) {
    const int magicSum = SIZE * (SIZE * SIZE + 1) / 2;

    for (int i = 0; i < SIZE; ++i) {
        int rowSum = 0, colSum = 0;
        for (int j = 0; j < SIZE; ++j) {
            rowSum += square[i][j];
            colSum += square[j][i];
        }
        if (rowSum != magicSum || colSum != magicSum) {
            return false;
        }
    }

    int diag1Sum = 0, diag2Sum = 0;
    for (int i = 0; i < SIZE; ++i) {
        diag1Sum += square[i][i];
        diag2Sum += square[i][SIZE - i - 1];
    }
    return diag1Sum == magicSum && diag2Sum == magicSum;
}

bool solveMagicSquare(int square[SIZE][SIZE], int x, int y, unordered_set<string>& visited) {
    if (isMagicSquare(square)) {
        return true;
    }
    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    for (int i = 0; i < 4; ++i) {
        int newX = x + dx[i];
        int newY = y + dy[i];

        if (isValidMove(newX, newY)) {
            swap(square[x][y], square[newX][newY]);
            string state = "";
            for (int i = 0; i < SIZE; ++i) {
                for (int j = 0; j < SIZE; ++j) {
                    state += to_string(square[i][j]);
                }
            }
            if (visited.find(state) == visited.end()) {
                visited.insert(state);
                if (solveMagicSquare(square, newX, newY, visited)) {
                    return true;
                }
            }
            swap(square[x][y], square[newX][newY]);
        }
    }
    return false;
}

int main() {
    int magicSquare[SIZE][SIZE];
    initializeSquare(magicSquare);

    srand(time(0));
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            int randomX = rand() % SIZE;
            int randomY = rand() % SIZE;
            swap(magicSquare[i][j], magicSquare[randomX][randomY]);
        }
    }

    cout << "Initial Puzzle:" << endl;
    printSquare(magicSquare);

    int movableX, movableY;
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            if (magicSquare[i][j] == SIZE * SIZE) {
                movableX = i;
                movableY = j;
                break;
            }
        }
    }

    unordered_set<string> visited;
    if (solveMagicSquare(magicSquare, movableX, movableY, visited)) {
        cout << "\nSolution:" << endl;
        printSquare(magicSquare);
    } else {
        cout << "\nNo solution found!" << endl;
    }

    return 0;
}
