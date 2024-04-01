import numpy as np
import matplotlib.pyplot as plt

def knapsack_value(solution, values, weights, max_weight):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_value += values[i]
            total_weight += weights[i]
            if total_weight > max_weight:
                return 0
    return total_value

def generate_initial_solution(num_items):
    return np.random.randint(2, size=num_items)

def generate_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        neighbor = solution.copy()
        neighbor[i] = 1 - neighbor[i]
        neighbors.append(neighbor)
    return neighbors

def hill_climbing_knapsack(values, weights, max_weight, max_iterations):
    current_solution = generate_initial_solution(len(values))
    current_value = knapsack_value(current_solution, values, weights, max_weight)
    global_max_value = current_value
    global_max_solution = current_solution.copy()
    global_min_value = float('inf')
    local_maxima = []
    local_minima = []

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        best_neighbor_value = -1
        best_neighbor_solution = None

        for neighbor in neighbors:
            neighbor_value = knapsack_value(neighbor, values, weights, max_weight)
            if neighbor_value > best_neighbor_value:
                best_neighbor_value = neighbor_value
                best_neighbor_solution = neighbor

        if best_neighbor_value == 0:
            break

        if best_neighbor_value > current_value:
            current_solution = best_neighbor_solution
            current_value = best_neighbor_value
            if current_value > global_max_value:
                global_max_value = current_value
                global_max_solution = current_solution.copy()
            local_maxima.append(current_value)
        else:
            local_minima.append(current_value)

    return global_max_solution, global_max_value, local_maxima, local_minima


values = [10, 20, 15, 25, 30]
weights = [2, 5, 7, 3, 1]
max_weight = 15
max_iterations = 10
best_solution, best_value, local_maxima, local_minima = hill_climbing_knapsack(values, weights, max_weight, max_iterations)
print("Best Solution:", best_solution)
print("Best Value:", best_value)
plt.plot(local_maxima, label='Local Maxima', marker='o', color='g')
plt.plot(local_minima, label='Local Minima', marker='x', color='r')
plt.xlabel('Iterations')
plt.ylabel('Knapsack Value')
plt.title('Local Maxima and Minima')
plt.legend()
plt.show()