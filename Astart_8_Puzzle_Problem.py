import heapq

class PuzzleNode:
    def _init_(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def _eq_(self, other):
        return self.state == other.state

    def _lt_(self, other):
        return (self.depth + self.heuristic()) < (other.depth + other.heuristic())

    def _hash_(self):
        return hash(str(self.state))

    def is_goal(self, goal_state):
        return self.state == goal_state

    def heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    row, col = divmod(self.state[i][j] - 1, 3)
                    distance += abs(i - row) + abs(j - col)
        return distance

    def get_possible_moves(self):
        possible_moves = []
        empty_row, empty_col = self.find_empty_tile()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in moves:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in self.state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = \
                    new_state[new_row][new_col], new_state[empty_row][empty_col]
                possible_moves.append((new_state, (new_row, new_col)))
        return possible_moves

    def find_empty_tile(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j


def reconstruct_path(node):
    path = []
    while node.parent:
        path.append(node.move)
        node = node.parent
    path.reverse()
    return path


def solve_8_puzzle(initial_state, goal_state):
    open_set = [PuzzleNode(initial_state)]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.is_goal(goal_state):
            return reconstruct_path(current_node)
        closed_set.add(current_node)

        for move_state, move in current_node.get_possible_moves():
            child = PuzzleNode(move_state, current_node, move)
            if child in closed_set:
                continue
            if child not in open_set:
                heapq.heappush(open_set, child)
            else:
                existing_node = open_set[open_set.index(child)]
                if child.depth < existing_node.depth:
                    existing_node.parent = current_node
                    existing_node.depth = child.depth

    return None

initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solution = solve_8_puzzle(initial_state, goal_state)
if solution:
    print("Solution found in {} steps:".format(len(solution)))
    for step, move in enumerate(solution, 1):
        print("Step {}: Move empty tile to {}".format(step, move))
else:
    print("No solution found.")