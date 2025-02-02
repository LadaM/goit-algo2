import math
import random


def sphere_function(x):
    return sum(xi ** 2 for xi in x)


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current_solution = [random.uniform(*bounds[i]) for i in range(dim)]
    current_value = func(current_solution)

    for _ in range(iterations):
        next_solution = [current_solution[i] + random.uniform(-0.1, 0.1) for i in range(dim)]
        next_solution = [
            max(bounds[i][0], min(bounds[i][1], next_solution[i])) for i in range(dim)
        ]
        next_value = func(next_solution)

        if next_value < current_value:
            current_solution, current_value = next_solution, next_value

        if abs(current_value - next_value) < epsilon:
            break

    return current_solution, current_value


def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best_solution = [random.uniform(*bounds[i]) for i in range(dim)]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate_solution = [random.uniform(*bounds[i]) for i in range(dim)]
        candidate_value = func(candidate_solution)

        if candidate_value < best_value:
            best_solution, best_value = candidate_solution, candidate_value

        if best_value < epsilon:
            break

    return best_solution, best_value


def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    current_solution = [random.uniform(*bounds[i]) for i in range(dim)]
    current_value = func(current_solution)

    for _ in range(iterations):
        temp *= cooling_rate
        next_solution = [current_solution[i] + random.uniform(-0.5, 0.5) for i in range(dim)]
        next_solution = [
            max(bounds[i][0], min(bounds[i][1], next_solution[i])) for i in range(dim)
        ]
        next_value = func(next_solution)

        if next_value < current_value or random.random() < math.exp((current_value - next_value) / max(temp, 1e-6)):
            current_solution, current_value = next_solution, next_value

        if temp < epsilon:
            break

    return current_solution, current_value


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
